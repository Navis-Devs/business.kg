from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from apps.accounts.utils import check_username
from apps.helpers.messages import mail_forgot, phone_forgot
from apps.helpers.send_mail import send_mail
from apps.helpers.send_sms import send_sms
from faker import Faker
from apps.accounts.models import User
fake = Faker()


class ForgotPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True
    )

    def validate(self, attrs):
        username = attrs.get("username")

        check = check_username(username)
        user = self.get_user(check)

        if not user:
            raise serializers.ValidationError("User with the given username does not exist.")

        new_password = fake.password()

        user.set_password(new_password)
        user.save()

        if check["type"] == "phone":
            send_sms(user.phone, phone_forgot(new_password))
        elif check["type"] == "email":
            send_mail(mail_forgot(user.email, new_password))
        else:
            raise serializers.ValidationError("Invalid username type")

        return attrs
    
    def get_user(self, check):
        if check["type"] == "email":
            return User.objects.filter(email=check["data"]).first()
        elif check["type"] == "phone":
            return User.objects.filter(profile__phone=check["data"]).first()  # Assuming phone is in a related profile model
        return None


class ForgotPasswordView(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response({
                "response": True,
                "message": "The password was successfully sent"
            })
        return Response(serializer.errors)