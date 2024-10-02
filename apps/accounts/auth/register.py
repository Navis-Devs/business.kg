from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password
from django.db.models import Q

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
        username = User.generate_unique_username()

        login = validated_data["username"]
        password = validated_data["password"]
        type = validated_data["type"]

        if type == "email":
            user = User(username=username, email=login)
        elif type == "phone":
            user = User(username=username, phone=login)

        user.set_password(password)
        user.save()
        return user


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # username = serializer.validated_data.get("username")
            # if User.objects.filter(Q(email=username) | Q(phone=int(username))).exists():
            #     return Response(
            #         {
            #             "response": False,
            #             "message": "A user with this name already exists.",
            #         },
            #     )

            user = serializer.save()
            # user = User.objects.get(username=serializer.validated_data.get("username"))

            ''' send activation code to email or phone number '''
            if serializer.validated_data.get("type") == "email":
                send_mail.send_mail(mail_registration(user.email, user.code))

            elif serializer.validated_data.get("type") == "phone":
                send_sms.send_sms(user.phone, phone_registration(user.code))

            else:
                return Response({"response": False, "message": "Not valid username"})

            return Response(
                {
                    "response": True,
                    "message": "The code was successfully sent"
                }
            )

        return Response(serializer.errors)
