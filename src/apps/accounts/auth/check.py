from rest_framework.response import Response
from rest_framework import serializers, generics
from apps.accounts.models import User
from apps.accounts.utils import check_username
from django.db.models import Q


class UserCheckSerializer(serializers.Serializer):
    username = serializers.CharField()

    class Meta:
        fields = ("username",)

    def validate(self, data):
        username = data.get("username")

        check_type = check_username(username)

        if not check_type:
            return {"response": False, "username": username, "user_exists": "Invalid username format"}

        login_type = check_type.get("type")
        username = check_type.get("data")

        if login_type == "email":
            exists = User.objects.filter(email=username).exists()
        elif login_type == "phone":
            exists = User.objects.filter(phone=username).exists()
        else:
            return {"response": False, "username": username, "user_exists": "Unknown login type"}

        return {"response": True, "username": username, "user_exists": exists}


class UserCheckView(generics.GenericAPIView):
    serializer_class = UserCheckSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
