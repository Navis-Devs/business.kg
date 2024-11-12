from rest_framework import serializers
from apps.main import models
from django.utils.timesince import timesince
from apps.house import mixins
from drf_writable_nested import WritableNestedModelSerializer



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
        fields = ['content_type', 'object_id', 'content_object', 'rating']
