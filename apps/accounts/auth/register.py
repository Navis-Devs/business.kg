from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password

from apps.accounts.models import User
from apps.accounts.utils import check_username
from apps.helpers.messages import mail_registration, phone_registration
from apps.helpers import send_mail, send_sms


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
    )

    confirm_password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "At least 8 characters"},
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "confirm_password",
        ]

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        check = check_username(username)

        if check:
            if check["type"] == "phone":
                attrs["username"] = check["data"]
                attrs["type"] = "phone"

            elif check["type"] == "email":
                attrs["username"] = check["data"]
                attrs["type"] = "email"

            else:
                raise serializers.ValidationError("Invalid username type")

        validate_password(password)

        if password != confirm_password:
            raise serializers.ValidationError("The passwords don't match")

        return attrs

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        user = User(username=username)
        user.set_password(password)
        user.save()
        return user


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if User.objects.filter(username=serializer.validated_data.get("username")).exists():
                return Response(
                    {
                        "response": False,
                        "message": "A user with this name already exists.",
                    },
                )

            serializer.save()
            user = User.objects.get(username=serializer.validated_data.get("username"))

            ''' send activation code to email or phone number '''
            if serializer.validated_data.get("type") == "email":
                send_mail.send_mail(mail_registration(user.username, user.code))

            elif serializer.validated_data.get("type") == "phone":
                send_sms.send_sms(user.username, phone_registration(user.code))

            else:
                return Response({"response": False, "message": "Not valid username"})

            return Response(
                {
                    "response": True,
                    "message": "The code was successfully sent"
                }
            )

        return Response(serializer.errors)
