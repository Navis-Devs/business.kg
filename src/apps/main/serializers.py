from rest_framework import serializers
from apps.main import models
from django.utils.timesince import timesince
from apps.house import mixins


class CommentSerializer(serializers.ModelSerializer):
    content = serializers.CharField(required=True)
    model = serializers.CharField()
    object_id = serializers.CharField()
    parent = serializers.IntegerField(required=False)

    class Meta:
        model = models.Comments
        fields = ['content', 'parent', 'model', 'object_id']

    def create(self, validated_data):
        model_name = validated_data.pop('model', None)
        object_id = validated_data.pop('object_id', None)
        parent_id = validated_data.pop('parent', None)

        try:
            content_type = models.ContentType.objects.get(model=model_name.lower())
            parent = None
            if parent_id:
                try:
                    parent = models.Comments.objects.get(id=parent_id)
                except models.Comments.DoesNotExist:
                    raise serializers.ValidationError({"detail": "Comment doesnt exists!"})

            comment = models.Comments.objects.create(
                user=self.context['request'].user,
                content_type=content_type,
                object_id=object_id,
                content=validated_data['content'],
                parent=parent
            )
        except models.ContentType.DoesNotExist:
            raise serializers.ValidationError({"model": "Wrong model name!"})
        return comment


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['name', '_avatar']


class CommentListSerializer(serializers.ModelSerializer, mixins.HierarchicalMixin):
    subcomment = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    user = UserInfoSerializer()

    class Meta:
        model = models.Comments
        fields = ['id', 'object_id', 'user', 'content', 'created_at', 'parent', 'subcomment']

    def get_subcomment(self, instance):
        return super().base_method(instance)

    def get_created_at(self, obj):
        return timesince(obj.created_at)
