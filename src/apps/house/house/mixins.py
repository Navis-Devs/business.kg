from apps.main import models
class HierarchicalMixin:
    
    def base_method(self, instance):
        """ Method to get child objects """
        if self.context.get('empty_㋡'):
            return None
        queryset = instance.get_children()
        if queryset.exists():
            return self.__class__(queryset, many=True).data
        return "empty ㋡"
    
class ViewsMixin:
    
    def get_views(self, instance):
        if instance:
            instance.views += 1
            result = instance
            result.save()

class BaseMixin:
    
    def get_comments(self, obj, serializer_class):
        content_type = models.ContentType.objects.get_for_model(obj.__class__)
        comments = models.Comments.objects.filter(parent=None, content_type=content_type, object_id=obj.id)
        return serializer_class(comments, many=True).data