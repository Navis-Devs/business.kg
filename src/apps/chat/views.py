from rest_framework import serializers
from django.utils.timesince import timesince
from rest_framework.generics import ListAPIView, RetrieveDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Room, Message
from .models import User

class RoomSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    avatar = serializers.SerializerMethodField(read_only=True)
    created_at = serializers.SerializerMethodField(read_only=True)
    last_message = serializers.SerializerMethodField(read_only=True)
    

    def get_avatar(self, obj):
        users = obj.users.all()  # Get all related users
        if users.count() > 1:
            second_user = users[1]  # Get the second user
            return f"https://business.navisdevs.ru{second_user._avatar.url}" if second_user._avatar else None
        return None

    def get_created_at(self, obj):
        return timesince(obj.created_at)
    
    def get_last_message(self, obj):
        last_message = Message.objects.filter(room=obj).order_by('-timestamp').first()
        if last_message:
            return last_message.text
        return None
    

class RoomCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Room
        fields = ['id', "name", 'users']
        
class ChatSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.email', read_only=True)
    user_id = serializers.CharField(source='sender.id', read_only=True)
    
    class Meta:
        model = Message
        fields = '__all__'
        
        
class ChatGetView(APIView):
    """Получить определенный чат"""
    def get(self, request, chat_id):
        user = request.user
        q = Message.objects.filter(room_id=chat_id, room__users=user)
        serializers = ChatSerializer(q, many=True).data
        return Response(serializers)
    
class RoomListView(ListAPIView):
    """Получить все чаты пользователя"""
    permission_classes = [IsAuthenticated, ]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    
    def get_queryset(self):
        user = self.request.user
        room = Room.objects.filter(users=user)
        return room

class RoomDeleteView(RetrieveDestroyAPIView):
    """Удалить чаты пользователя"""
    permission_classes = [IsAuthenticated, ]
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        user = self.request.user
        room = Room.objects.filter(users=user)
        return room
    
class RoomCreateView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomCreateSerializer
    permission_classes = [IsAuthenticated,]
    
    def perform_create(self, serializer):
        users = serializer.validated_data.get('users', [])
        users.append(self.request.user)
        serializer.save(users=users)
