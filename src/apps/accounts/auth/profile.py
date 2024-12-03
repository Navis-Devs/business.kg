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
from apps.house.serializers import PropertySerializer, UserInfoSerializer
from apps.house.models import Property
from apps.cars_posts.models import CarsPosts
from apps.cars_posts.serializers import CarsPostsDetailSerializer
from apps.helpers.paginations import StandardPaginationSet
'''
SERIALIZERS PART
'''
class ProfileSerializer(serializers.ModelSerializer):
    # date_joined = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    _avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "username", 'mkg_id', "phone", "email", "name", "is_active", "_avatar", "balance", "language")

    def get__avatar(self, obj):
        if obj._avatar:
            return f"https://business.navisdevs.ru{obj._avatar.url}"
        return None

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
        if not user or not user.is_authenticated:
            return Response({"detail": "Authentication required."}, status=401)

        print(user.email)

        car_data = CarsPostsDetailSerializer(
            CarsPosts.objects.filter(user=user),
            many=True,
            context={'request': request} 
        ).data

        property_data = PropertySerializer(
            Property.objects.filter(user=user),
            many=True,
            context={'request': request} 
        ).data

        ads = {"house": property_data, "car": car_data}

        data = self.serializer_class(user).data
        data["dates"] = {
            "date_joined": f"{user.date_joined}",
            "last_login": f"{user.last_login}",
            "ads": ads
        }
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



class AccountInfo(viewsets.GenericViewSet):
    serializer_class = UserInfoSerializer
    queryset = User.objects.all()
    pagination_class = StandardPaginationSet
    
    @action(methods=['get'], detail=True)
    def user_info(self, request, pk=None):
        user = self.get_object()
        user_data = self.get_serializer(user).data
        car_data = CarsPostsDetailSerializer(CarsPosts.objects.filter(user=user), many=True, context={'request': request}).data
        property_data = PropertySerializer(Property.objects.filter(user=user), many=True, context={'request': request}).data

        
        ads = {"house": property_data, "car": car_data}
        
        response = {**user_data, "ads": ads}
        
        return Response(response)