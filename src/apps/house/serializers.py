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
            ('big', 'url'),
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
    price = serializers.IntegerField(required=True, write_only=True)
    currency = serializers.IntegerField(required=True, write_only=True)
    square = serializers.IntegerField(required=True)

    class Meta:
        model = models.Property
        fields = '__all__' 
        
    
    def create(self, validated_data):
        many_to_many_fields = [
            'land_amenities', 'likes',
            'land_options', 'flat_options',
            'safety', 'documents',
            'room_option', 'options',
            'room_options'
        ]
        many_to_many_data = {field: validated_data.pop(field, []) for field in many_to_many_fields}
        object_price = validated_data.pop('price')
        object_square = validated_data.pop('square')
        object_currency_id = validated_data.pop('currency')  
        
        try:
            object_currency = models.Currency.objects.get(id=object_currency_id)
        except models.Currency.DoesNotExist:
            raise serializers.ValidationError(f"Currency with id {object_currency_id} does not exist.")
        
        validated_data['square'] = object_square

        instance_model = models.Property.objects.create(**validated_data)
        conversion_rate = 86 
        prices = []

        if object_currency.id == 1:  
            usd_price = object_price * conversion_rate
            usd_price_per_m2 = usd_price / object_square

            prices.append(models.Price(
                property=instance_model,
                price=object_price,
                m2_price=object_price / object_square,
            ))

            prices.append(models.Price(
                property=instance_model,
                price=usd_price,
                m2_price=usd_price_per_m2,
            ))

        elif object_currency.id == 2: 
            som_price = object_price * conversion_rate
            som_price_per_m2 = som_price / object_square

            prices.append(models.Price(
                property=instance_model,
                price=object_price,
                m2_price=object_price / object_square,
            ))

            prices.append(models.Price(
                property=instance_model,
                price=som_price,
                m2_price=som_price_per_m2,
            ))

        models.Price.objects.bulk_create(prices)

        for field, values in many_to_many_data.items():
            if values:
                getattr(instance_model, field).set(values)

        return instance_model
        
class UserInfoSerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)
    avarage_rating = serializers.FloatField(read_only=True, default='4.5')
    accommodation_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.User
        fields = ['id', 'name', 'review_count', 'avarage_rating', 'accommodation_count', '_avatar', 'phone', 'description']
    
class PropertySerializer(serializers.ModelSerializer, mixins.BaseMixin):
    user = UserInfoSerializer(read_only=True)
    added_at = serializers.SerializerMethodField()
    properties_pictures = PicturesSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    count_comments = serializers.SerializerMethodField()
    prices = PriceSerializer(many=True)
    phones = PhonesSerializer(many=True)
    phone = serializers.IntegerField(source='user.phone', read_only=True)
    likes = serializers.IntegerField(source="likes.count", read_only=True)
    is_liked = serializers.SerializerMethodField()
    count_comments = serializers.IntegerField(source='comments_count', read_only=True)

    class Meta:
        model = models.Property
        fields = '__all__'

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user in obj.likes.all()

    def get_comments(self, obj):
        return super().get_comments(obj, CommentListSerializer)
    
    def get_added_at(self, obj):
        return timesince(obj.created_at)


class PropertyListSerializer(serializers.ModelSerializer):
    properties_pictures = PicturesSerializer(many=True)
    prices = PriceSerializer(many=True, read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = models.Property
        fields = [
            'id', 'prices', 'properties_pictures', 'type_id', 'category',
            'rooms', 'square', 'floor', 'floors', 'is_liked', 
            'autoup_time', 'autoup_until', 'vipped_until', 'premium_until', 'premium_gradient', 
            'premium_dark_gradient',
            'urgent_until', 'topped_until', 'ad_color', 'ad_dark_color', 'colored_until',
            'is_vip', 'is_premium', 'is_autoup', 'is_urgent', 'featured', 'is_top',
        ]

    def get_is_liked(self, obj):
        user = self.context.get('request').user
        return user in obj.likes.all()