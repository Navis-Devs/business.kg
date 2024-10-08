from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )
    confirm_password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )


class ChangePasswordView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        user = request.user
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            password = serializer.data["password"]
            confirm_password = serializer.data["confirm_password"]

            if password != confirm_password:
                return Response({"response": False, "message": "Пароли не совпадают"})

            user.set_password(password)
            user.save()

            return Response({"response": True, "message": "Пароль успешно обновлен"})
        return Response(serializer.errors)
