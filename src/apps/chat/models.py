from django.db import models
from apps.accounts.models import User

class Room(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,  related_name='user')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    read = models.BooleanField(default=False)