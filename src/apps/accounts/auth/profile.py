from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

import os
import io
import uuid
import base64
import requests

from PIL import Image
from django.conf import settings
from user_agents import parse

from apps.helpers.exceptions import BadRequest
from apps.accounts.models import User

'''
SERIALIZERS PART
'''
class ProfileSerializer(serializers.ModelSerializer):
    # date_joined = serializers.DateTimeField(format='%d.%m.%Y %H:%M')

    class Meta:
        model = User
        fields = ("id", "username", "phone", "email", "name", "is_active", "_avatar", "balance", "language")


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "language")


class UserAvatarSerializer(serializers.Serializer):
    image = serializers.CharField(write_only=True)

    def create(self, validated_data):
        image = validated_data.get('image')
        if image is None:
            raise BadRequest("Нет фото")

        user = self.context['request'].user
        full_path = f"{settings.MEDIA_ROOT}/user/{user.id}"

        if not os.path.exists(full_path):
            os.makedirs(full_path)

        filename = f"{str(uuid.uuid4())}.png"

        img = Image.open(io.BytesIO(base64.decodebytes(bytes(image, "utf-8"))))
        img.save(f"{full_path}/{filename}")
        user._avatar = f"user/{user.id}/{filename}"
        user.save()

        return user

'''
VIEWS PART
'''
class ProfileViewSet(
        viewsets.GenericViewSet,
    ):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'patch': return ProfileUpdateSerializer
        if self.action == 'avatar': return UserAvatarSerializer
        return self.serializer_class

    @action(methods=['get'], permission_classes=[IsAuthenticated], detail=False)
    def me(self, request):
        user = request.user

        data = self.serializer_class(user).data
        data["dates"] = {
            "date_joined": f"{user.date_joined}",
            "last_login": f"{user.last_login}",
        }
        ip_data = requests.get(f"http://ipapi.co/{request.META.get('REMOTE_ADDR')}/json")
        if ip_data.status_code == 200:
            ip_data = ip_data.json()
            data["ipAddress"] = {
                "ip": ip_data.get("ip"),
                "country_name": ip_data.get("country_name"),
                "country_code": ip_data.get("country_code"),
                "continent_code": ip_data.get("continent_code"),
                "timezone": ip_data.get("timezone"),
                "city": ip_data.get("city"),
                "region": ip_data.get("region"),
            }
        user_agent_string = request.headers.get('User-Agent', '')
        user_agent = parse(user_agent_string)
        data["deviceInfo"] = {
            "os": user_agent.os.family,
            "browser": user_agent.browser.family,
            "device_brand": user_agent.device.brand,
            "device_model": user_agent.device.model,
            "is_mobile": user_agent.is_mobile,
            "is_tablet": user_agent.is_tablet,
            "is_pc": user_agent.is_pc,
            "is_touch_capable": user_agent.is_touch_capable,
        }
        data["list"] = [1, 2, 3, {"key": "value"}]
        return Response(data)

    @action(methods=['patch'], permission_classes=[IsAuthenticated], detail=False, url_path='update')
    def patch(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['POST'], permission_classes=[IsAuthenticated], detail=False, url_path='avatar')
    def avatar(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(ProfileSerializer(request.user).data)
