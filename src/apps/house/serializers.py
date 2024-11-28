from rest_framework import serializers
from apps.house import models
from apps.main.models import Review
from apps.house import mixins
from apps.main.models import Comments, ContentType
from drf_writable_nested import WritableNestedModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer
from apps.main.serializers import CommentListSerializer
from django.utils.timesince import timesince
from rest_framework_gis.serializers import GeoModelSerializer
from apps.house import exceptions

class BuildingPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BuildingPrice
        fields = '__all__'

class BuildingImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BuildingImage
        fields = '__all__'

class BuildingsSerializer(serializers.ModelSerializer):
    images = BuildingImagesSerializer(many=True)
    prices = BuildingPriceSerializer(many=True)
    class Meta:
        model = models.Building
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        comment_count = instance.reviews.count()
        avarage_rating = Review.get_average_rating(instance)
        representation['review_count'] = comment_count
        representation['avarage_rating'] = float(avarage_rating)
        return representation   
        
class PicturesSerializer(serializers.ModelSerializer):
    pictures = VersatileImageFieldSerializer(
        sizes=[
            ('thumbnail', 'crop__100x100'),  
            ('small', 'crop__200x200'),      
            ('medium', 'crop__400x400'),     
            ('big', 'url')
        ]
    )
    class Meta:
        model = models.Pictures
        fields = ['pictures', ]
        
class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Price
        fields = '__all__'
        
class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phones
        fields = ['phones']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation['phones']
        
class AddPropertySerializer(WritableNestedModelSerializer):
    properties_pictures = PicturesSerializer(many=True, required=False)
    class Meta:
        model = models.Property
        fields = '__all__' 
        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'name', '_avatar', 'phone']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        posted_count = models.Property.objects.filter(user=instance).count()
        comment_count = instance.reviews.count()
        avarage_rating = Review.get_average_rating(instance)
        representation['name'] = representation['name'] if representation['name'] else 'пользователь'
        representation['review_count'] = comment_count
        representation['avarage_rating'] = float(avarage_rating)
        representation['accommodation_count'] = posted_count
        return representation
    
class PropertySerializer(GeoModelSerializer, serializers.ModelSerializer, mixins.BaseMixin):
    user = UserInfoSerializer()
    added_at = serializers.SerializerMethodField()
    properties_pictures = PicturesSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    count_comments = serializers.SerializerMethodField()
    prices = PriceSerializer(many=True)
    phones = PhonesSerializer(many=True)
    likes = serializers.IntegerField(source="likes.count", read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = models.Property
        geo_field = "point"
        fields = '__all__'

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user in obj.likes.all()

    def get_comments(self, obj):
        return super().get_comments(obj, CommentListSerializer)
    
    def get_added_at(self, obj):
        return timesince(obj.created_at)
    
    def get_count_comments(self, obj):
        comment_instance = Comments.objects.filter(object_id=obj.id).first()
        return comment_instance.count_comment if comment_instance else 0