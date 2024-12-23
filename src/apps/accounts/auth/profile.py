from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.db.models import Prefetch
from django.db.models import Count, Avg, F
from django.core.cache import cache

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
from apps.house.serializers import PropertyListSerializer, UserInfoSerializer
from apps.house.models import Property
from apps.cars_posts.models import CarsPosts, CarPrices
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
        fields = ("name", "language", "email", "phone")

class UserAvatarSerializer(serializers.Serializer):
    _avatar = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ("_avatar",)

    def create(self, validated_data):
        user = self.context['request'].user
        user._avatar = validated_data['_avatar']
        user.save()
        return user


    # def create(self, validated_data):
    #     image = validated_data.get('image')
    #     if image is None:
    #         raise BadRequest("Нет фото")

    #     user = self.context['request'].user
    #     full_path = f"{settings.MEDIA_ROOT}/user/{user.id}"

    #     if not os.path.exists(full_path):
    #         os.makedirs(full_path)

    #     filename = f"{str(uuid.uuid4())}.png"

    #     img = Image.open(io.BytesIO(base64.decodebytes(bytes(image, "utf-8"))))
    #     img.save(f"{full_path}/{filename}")
    #     user._avatar = f"user/{user.id}/{filename}"
    #     user.save()

    #     return user

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
        
        car_data = CarsPostsDetailSerializer(
            CarsPosts.objects.filter(user=user).select_related
            (
                'mark',
                'model', 
                'generation_id',
                'modification_id',
                'serie_id',
                'dealer_id',
                'region',
                'town'
                ).prefetch_related(
                    'car_condition',
                ),
            many=True,
            context={'request': request} 
        ).data

        property_data = PropertyListSerializer(
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
    
    
    def get_queryset(self):
        return User.objects.annotate(
            average_rating=Avg('reviews__rating'),
            property_count=Count('property', distinct=True),
            carsposts_count=Count('carsposts', distinct=True)
        ).annotate(
            accommodation_count=F('property_count') + F('carsposts_count')
        )

    @action(methods=['get'], detail=True)
    def user_info(self, request, pk=None):
        user = self.get_object()
        user_data = self.get_serializer(user).data
        car_data = CarsPostsDetailSerializer(
            CarsPosts.objects.filter(user=user).select_related(
                "user",
                "model",
                "mark",
                "car_type",
            ).prefetch_related(
                "likes",
                "configuration",
                "interior",
                "exterior",
                "media",
                "safety",
                "other_options",
                "prices",
                "pictures",
            ),
            many=True,
            context={'request': request}
        ).data
        
        property_data = PropertyListSerializer(
            Property.objects.filter(user=user).select_related(
                "user",
            ).prefetch_related(
                "likes",
                "safety",
                "flat_options",
                "documents",
                "room_options",
                "options",
                "land_options",
                "land_amenities",
                "prices",
                "phones",
                "comments",
            ),
            many=True,
            context={'request': request}
        ).data

        ads = {"house": property_data, "car": car_data}
        response = {**user_data, "ads": ads}
        

        return Response(response)