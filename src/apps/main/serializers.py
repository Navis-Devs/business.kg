from rest_framework import serializers
from apps.main import models
from django.utils.timesince import timesince
from apps.house import mixins
from drf_writable_nested import WritableNestedModelSerializer
from apps.accounts.models import Dealer, DealerImages
from apps.house.models import Property
from apps.cars_posts.models import CarsPosts

class CommentSerializer(WritableNestedModelSerializer):
    content = serializers.CharField(required=True)
    model = serializers.CharField()
    object_id = serializers.CharField()
    parent = serializers.IntegerField(required=False)
    
    class Meta:
        model = models.Comments
        fields = ['content', 'parent', 'model', 'object_id']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', 'name', '_avatar']

class CommentListSerializer(serializers.ModelSerializer, mixins.HierarchicalMixin):
    subcomment = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    user = UserInfoSerializer()

    class Meta:
        model = models.Comments
        fields = ['id', 'count_comment', 'object_id', 'user', 'content', 'created_at', 'parent', 'subcomment']
    
    def get_subcomment(self, instance):
        return super().base_method(instance)
    
    def get_created_at(self, obj):
        return timesince(obj.created_at)

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Review
        fields = ['content_type', 'object_id', 'rating', 'comment']

class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SearchHistory
        fields = ['search_query', 'filter_params', 'created_at']

class DealerListSerializer(serializers.ModelSerializer):
    review_count = serializers.IntegerField(source='reviews.count', read_only=True, default=0)
    avarage_rating = serializers.FloatField(read_only=True, default=5.0)
    ads_count = serializers.IntegerField(read_only=True, default=0)
    class Meta:
        model = Dealer
        fields = ['id', 'logo_path', 'name', 'ads_count', 'avarage_rating', 'review_count', 'is_verified', 'address']

class DealerImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerImages
        fields = '__all__'


class DealerSerializer(serializers.ModelSerializer):
    dealer_images = DealerImagesSerializer(many=True, read_only=True)
    class Meta:
        model = Dealer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = instance.user
        property_count = Property.objects.filter(user=user).count()
        cars_count = CarsPosts.objects.filter(user=user).count()
        ads_count = property_count + cars_count
        comment_count = instance.reviews.count()
        avarage_rating = models.Review.get_average_rating(instance)
        representation['name'] = representation.get('name', 'пользователь') or 'пользователь'
        representation['review_count'] = comment_count
        representation['avarage_rating'] = float(avarage_rating) 
        representation['ads_count'] = ads_count

        return representation
