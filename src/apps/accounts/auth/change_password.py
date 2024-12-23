from rest_framework import serializers, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )
    new_password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )
    confirm_password = serializers.CharField(
        required=True,
        min_length=8,
        error_messages={"min_length": "Не менее 8 символов.", "required": "Это поле обязательно."}
    )

    def validate(self, attrs):
        user = self.context['request'].user
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if not user.check_password(old_password):
            raise serializers.ValidationError("Братан, cтарый пароль введён неверно")
        if old_password == new_password:
            raise serializers.ValidationError("Новый пароль не может совпадать с текущим.")
        if new_password != confirm_password:
            raise serializers.ValidationError("Пароли не совпадают.")
        
        return attrs


class ChangePasswordView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})

        if serializer.is_valid():
            user = request.user
            new_password = serializer.validated_data["new_password"]
            
            user.set_password(new_password)
            user.save()

            return Response({"response": True, "message": "Пароль успешно обновлен"}, status=200)

        return Response(serializer.errors, status=400)
