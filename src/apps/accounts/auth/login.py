from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate
# local imports

from django.contrib.auth import get_user_model

from apps.accounts.utils import check_username

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        write_only=True,
        required=True,
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
    )
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.get("username")
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
        return attrs


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            password = serializer.validated_data.get("password")
            type = serializer.validated_data.get("type")

            try:
                if type == "email":
                    user = User.objects.get(email=username)
                elif type == "phone":
                    user = User.objects.get(phone=username)

                else:
                    return Response({
                        "response": False,
                        "message": "Invalid username"}
                    )
                if not user.is_active:
                    return Response(
                        {
                            "response": False,
                            "message": "Confirm your account before logging in",
                        }
                    )
            except ObjectDoesNotExist:
                return Response(
                    {
                        "response": False,
                        "message": "No such user exists",
                    }
                )

            user = authenticate(request, username=user.username, password=password)

            if not user:
                return Response(
                    {
                        "response": False,
                        "message": "Invalid password or login",
                    }
                )

            if user.is_active:
                token, created = Token.objects.get_or_create(user=user)
                return Response(
                    {
                        "response": True,
                        "message": "The login was successful",
                        "token": token.key,
                        "type": "Token"
                    }
                )

        return Response(serializer.errors)
