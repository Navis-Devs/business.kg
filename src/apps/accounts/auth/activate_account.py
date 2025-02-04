from rest_framework import serializers, generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.exceptions import ObjectDoesNotExist

from apps.accounts.utils import check_username

from django.contrib.auth import get_user_model
User = get_user_model()


class ActivateAccountSerializer(serializers.Serializer):
    username = serializers.CharField(
        required=True,
    )
    code = serializers.IntegerField(
        required=True
    )

    class Meta:
        fields = ["username", "code"]

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
                raise serializers.ValidationError("Некорректный тип активации.")
        return attrs


class ActivateAccountView(generics.GenericAPIView):
    serializer_class = ActivateAccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get("username")
            code = serializer.validated_data.get("code")
            type = serializer.validated_data.get("type")

            try:
                if type == "email":
                    user = User.objects.get(email=username)
                elif type == "phone":
                    user = User.objects.get(phone=username)

                if user.is_active:
                    return Response({"response": False, "message": "Этот аккаунт уже активен."})

                if user.code == code:
                    user.is_active = True
                    user.save()

                    token, created = Token.objects.get_or_create(user=user)

                    return Response(
                        {
                            "response": True,
                            "message": "Аккаунт был успешно активирован.",
                            "token": token.key,
                            "type": "Token",
                        }
                    )
                return Response(
                    {"response": False, "message": "Код введен неверно."}
                )
            except ObjectDoesNotExist:
                return Response(
                    {
                        "response": False,
                        "message": "Такой пользователь не найден в системе или неактивный.",
                    }
                )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
