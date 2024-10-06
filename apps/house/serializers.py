from rest_framework import serializers
from apps.house import models
from apps.house import mixins
from drf_writable_nested import WritableNestedModelSerializer
from apps.helpers.api.models import Currency
from versatileimagefield.serializers import VersatileImageFieldSerializer
from apps.main.serializers import CommentListSerializer


class ResidentialCategorySerializer(serializers.ModelSerializer, mixins.HierarchicalMixin):
    children = serializers.SerializerMethodField()

    class Meta:
        model = models.ResidentialCategory
        fields = ['id', 'complex_name', 'building_date', 'level', 'parent', 'children']

    def get_children(self, instance):
        return super().base_method(instance)


class MiscellaneousSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Miscellaneous
        fields = '__all__'


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Security
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Documents
        fields = '__all__'


class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Communication
        fields = '__all__'


class RegionsSerializer(serializers.ModelSerializer, mixins.HierarchicalMixin):
    class Meta:
        model = models.Location
        fields = [
            'id',
            'city', 'lat',
            'lng', 'population',
            'iso2', 'capital', 'lft',
            "rght", "tree_id", "level", "parent",
        ]


class PicturesListSerializer(serializers.ModelSerializer):
    pictures = VersatileImageFieldSerializer(
        sizes=[
            ('medium_size', 'crop__400x400')
        ]
    )

    class Meta:
        model = models.Pictures
        fields = ['pictures', ]


class PicturesDetailSerializer(serializers.ModelSerializer):
    pictures = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
        ]
    )

    class Meta:
        model = models.Pictures
        fields = ['pictures', ]


class AddPropertySerializer(WritableNestedModelSerializer):
    id = serializers.CharField(source='hashid', read_only=True)
    security = SecuritySerializer(required=False)
    miscellaneous = MiscellaneousSerializer(required=False)
    documents = DocumentsSerializer(required=False)
    communication = CommunicationSerializer(required=False)
    properties_pictures = PicturesDetailSerializer(many=True, required=False)

    class Meta:
        model = models.Property
        fields = [
            'id',
            'type_deal',
            'type_property',
            'room_count', 'type_series',
            'type_building', 'year_construction',
            'floor_number', 'total_floors', 'general',
            'residential', 'kitchen', 'land_area', 'type_heating', 'type_condition',
            'eni_code', 'street', 'house_number', 'intersection_with', 'lat',
            'lon', 'youtube_url', 'description', 'description', 'location', 'price', 'currency', 'price_for',
            'installment_type',
            'mortage_type', 'exchange_type', 'advertiser_type', 'phone_number', 'floor', 'internet', 'gas', 'furniture',
            'front_door',
            'balkony', 'parking', 'bathroom', 'disposition_object', 'electricity', 'sewage', 'drinking_water',
            'phone_connection',
            'complex_name',
            'security',
            "miscellaneous",
            'documents',
            'communication',
            'properties_pictures',
        ]


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['username', '_avatar']


class PropertyDetailSerializer(serializers.ModelSerializer, mixins.BaseMixin):
    user = UserInfoSerializer()
    id = serializers.CharField()
    properties_pictures = PicturesDetailSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()

    class Meta:
        model = models.Property
        fields = [
            'id', 'user', 'type_deal', 'type_property', 'room_count',
            'type_series', 'type_building', 'year_construction',
            'floor_number', 'total_floors', 'general', 'residential',
            'kitchen', 'land_area', 'type_heating', 'type_condition',
            'eni_code', 'street', 'house_number', 'intersection_with',
            'lat', 'lon', 'youtube_url', 'description', 'price',
            'currency', 'price_for', 'installment_type', 'mortage_type',
            'exchange_type', 'advertiser_type', 'phone_connection',
            'drinking_water', 'sewage', 'electricity', 'disposition_object',
            'bathroom', 'parking', 'balkony', 'front_door', 'furniture',
            'gas', 'internet', 'floor', 'phone_number', 'views',
            'location', 'security', 'miscellaneous', 'documents',
            'communication', 'complex_name', 'properties_pictures', 'comments'
        ]
        depth = 1

    def get_comments(self, obj):
        return super().get_comments(obj, CommentListSerializer)


class PropertyListSerializer(serializers.ModelSerializer, mixins.BaseMixin):
    id = serializers.CharField()
    properties_pictures = serializers.SerializerMethodField()
    location = RegionsSerializer()
    description = serializers.SerializerMethodField()
    _usd_course = serializers.SerializerMethodField()

    class Meta:
        model = models.Property
        fields = [
            'id', 'type_property', 'room_count', 'general', 'land_area',
            'street', 'house_number', 'description', 'price', 'currency', 'location', 'views', '_usd_course',
            'properties_pictures'
        ]

    def get_description(self, instance):
        if hasattr(instance, 'description') and instance.description:
            return self.shortener_world(instance, 'description')
        return None

    def get__usd_course(self, instance):
        instance = Currency.objects.first()
        return instance.usd_course if instance and instance.usd_course else 'System error fx.kg'

    def get_properties_pictures(self, obj):
        return PicturesListSerializer(obj.properties_pictures.first()).data \
            if obj.properties_pictures.exists() else None
