from rest_framework import serializers
from versatileimagefield.serializers import VersatileImageFieldSerializer
from .models import CarsPosts, Media, Exterior, Interior, Safety, GeneralOptions, Pictures, CarPrices, User, Review, GeneralOptions, OtherOptions
from drf_writable_nested import WritableNestedModelSerializer
from apps.main.serializers import CommentListSerializer
from apps.main.models import Comments 
from django.utils.timesince import timesince
from apps.house import mixins

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = '__all__'


class ExteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exterior
        fields = '__all__'


class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = '__all__'


class SafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = Safety
        fields = '__all__'


class GeneralOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralOptions
        fields = '__all__'


class PicturesSerializer(serializers.ModelSerializer):
    pictures = VersatileImageFieldSerializer(
        sizes=[
            ('small', 'crop__400x400'),     
            ('big', 'url')
        ]
    )
    class Meta:
        model = Pictures
        fields = ['pictures', ]


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPrices
        fields = ['price', ]

class AdCarsPostsSerializer(WritableNestedModelSerializer):
    pictures = PicturesSerializer(many=True, write_only=True, required=False)
    class Meta:
        model = CarsPosts
        fields = '__all__'

class UserInfoSerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)
    avarage_rating = serializers.FloatField(read_only=True, default='4.5')
    accommodation_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'review_count', 'avarage_rating', 'accommodation_count', '_avatar', 'phone', 'description']


class CarsPostsDetailSerializer(serializers.ModelSerializer, mixins.BaseMixin):
    # read only
    car_type_name = serializers.CharField(source="car_type.name", read_only=True)
    mark_name = serializers.CharField(source="mark.name", read_only=True)
    model_name = serializers.CharField(source="model.name", read_only=True)
    serie_name = serializers.CharField(source="serie.name", read_only=True)
    modification_name = serializers.CharField(source="modification.name", read_only=True)
    pictures = PicturesSerializer(many=True, read_only=True)
    user = UserInfoSerializer(read_only=True)
    prices = PriceSerializer(many=True, read_only=True)
    added_at = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    count_comments = serializers.IntegerField(source='comments_count', read_only=True)
    

    # additional
    likes = serializers.IntegerField(source="likes.count", read_only=True)
    is_liked = serializers.SerializerMethodField()
    class Meta:
        model = CarsPosts
        fields = '__all__'

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user in obj.likes.all()
    
    def get_comments(self, obj):
        return super().get_comments(obj, CommentListSerializer)
    
    def get_added_at(self, obj):
        return timesince(obj.created_at)

class CarsPostsListSerializer(serializers.ModelSerializer):
    mark_name = serializers.CharField(source="mark.name", read_only=True)
    model_name = serializers.CharField(source="model.name", read_only=True)
    pictures = PicturesSerializer(many=True, read_only=True)
    prices = PriceSerializer(many=True, read_only=True)
    dealer_name = serializers.CharField(source='dealer.name', read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = CarsPosts
        fields = ['id', 'is_vip', 'is_premium', 'is_autoup', 'is_urgent', 'featured', 'is_top',
                 'mark_name', 'model_name', 'dealer_name', 'pictures', 'year', 'mileage', 'mileage_unit', 'prices', 'is_liked',
                 'autoup_time', 'autoup_until', 'vipped_until', 'premium_until', 'premium_gradient', 'premium_dark_gradient',
                 'urgent_until', 'topped_until', 'ad_color', 'ad_dark_color', 'colored_until'
                 ]

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user in obj.likes.all()