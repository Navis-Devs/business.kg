from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from mptt.models import MPTTModel, TreeForeignKey
from apps.accounts.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Avg

class Comments(MPTTModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcomment')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    comment_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.parent:
            self.parent.comment_count = Comments.objects.filter(parent=self.parent).count()
            self.parent.save()
        super().save(*args, **kwargs)
    
    class MPTTMeta:
        order_insertion_by = ['content']
    
    def __str__(self):
        return self.content

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField(max_length=200)
    content_object = GenericForeignKey('content_type', 'object_id')
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    comment = models.TextField()
    
    @staticmethod
    def get_average_rating(instance):
        reviews = instance.reviews.all()
        if reviews.exists():
            return reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        return 0
    

class SearchHistory(models.Model):
    type_choices = [
        ('car', 'car'),
        ('house', 'house')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    search_query = models.CharField(max_length=255, blank=True, null=True)
    filter_params = models.JSONField(blank=True, null=True)
    type = models.CharField(max_length=50, null=True, blank=True, choices=type_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Фильтрация по {self.user.username} at {self.timestamp}"