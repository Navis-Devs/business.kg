from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
import json
from .models import Message

from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
import json
from .models import Message, Room
from apps.accounts.models import User
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Room, Message
from channels.db import database_sync_to_async

# @database_sync_to_async
# def get_or_create_private_room(user1, user2):
#     # Создаём имя комнаты на основе пользователей
#     room_name = f'private_{min(user1.username, user2.username)}_{max(user1.username, user2.username)}'
    
#     # Ищем комнату по имени
#     room = Room.objects.filter(name=room_name).first()

#     if not room:
#         # Если комната не найдена, создаем новую
#         room = Room.objects.create(name=room_name)
#         # Добавляем обоих пользователей в комнату
#         room.users.add(user1, user2)
    
#     return room



# for create  андрей создает комнату отправляя id Саши и свой токен 
#  ws://127.0.0.1:8000/ws/chat/d1443126-9c6f-462f-b4fd-57e5d8a306a2/private_chat/?token=5bc03905e2f896e6f031204193dc75737c0f765b

# for receive chat Саша получит увидет в чате что кто то написал и отправит "name" /private_Andrei_Sasha/ и свой токен 
# ws://127.0.0.1:8000/ws/chat/d1443126-9c6f-462f-b4fd-57e5d8a306a2/private_Andrei_Sasha/?token=5bc03905e2f896e6f031204193dc75737c0f765b



# class ChatConsumer(AsyncWebsocketConsumer):
    
#     async def connect(self):
#         self.user = self.scope["user"]
#         target_user_id = self.scope['url_route']['kwargs'].get('target_user_id')  # ID второго пользователя
#         print("ID переданного пользователя: ", target_user_id)
#         if self.user.is_anonymous:
#             await self.close()
#         else:
#             target_user = await database_sync_to_async(User.objects.get)(id=target_user_id)
#             if not target_user:
#                 await self.close()
#                 return

#             self.room = await get_or_create_private_room(self.user, target_user)
#             self.room_group_name = f'chat_{self.room.name}'

#             # Подключаем к группе
#             await self.channel_layer.group_add(
#                 self.room_group_name,
#                 self.channel_name
#             )
#             await self.accept()
            
#     async def disconnect(self, close_code):
#         if hasattr(self, 'room_group_name'):
#             await self.channel_layer.group_discard(
#                 self.room_group_name,
#                 self.channel_name
#             )

#     async def receive(self, text_data):
#         user = self.scope["user"]

#         if user.is_anonymous:
#             return

#         data = json.loads(text_data)
#         message_text = data.get('message', '')

#         # Сохраняем сообщение
#         await database_sync_to_async(Message.objects.create)(
#             sender=user,
#             room=self.room,
#             text=message_text
#         )

#         # Отправляем сообщение в группу
#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message_text,
#                 'sender': user.username,
#             }
#         )


#     async def chat_message(self, event):
#         message = event['message']
#         sender = event['sender']

#         await self.send(text_data=json.dumps({
#             'message': message,
#             'sender': sender,
#         }))


# @database_sync_to_async
# def create_room(room_name):

    

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_id = self.scope['url_route']['kwargs']['room_id']
#         self.room_group_name = f'chat_{self.room_id}'

#         await self.channel_layer.group_add(
#             self.room_group_name,
#             self.channel_name
#         )

#         await self.accept()
#         self.first_message_received = True

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         data = json.loads(text_data)
#         user = self.scope["user"]

#         if not user.is_authenticated:
#             await self.close()
#             return
#         if not self.first_message_received:
#             self.first_message_received = True
#             await self.first_seen_message(message)
#         else:
#             await self.second_seen_message(message)

#         text = data['message']
#         message = await self.save_message(self.room_id, user.id, text)

#         await self.channel_layer.group_send(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message,
#             }
#         )

#     async def chat_message(self, event):
#         await self.send(text_data=json.dumps(event['message']))

#     @database_sync_to_async
#     def save_message(self, room_id, sender_id, text):
#         room = Room.objects.get(id=room_id)
#         sender = User.objects.get(id=sender_id)
#         message = Message.objects.create(room=room, sender=sender, text=text)
#         return {
#             'id': message.id,
#             'sender': sender.username,
#             'text': message.text,
#             'timestamp': str(message.timestamp),
#             'first_seen_message': message.first_seen_message,
#             'second_seen_message': message.second_seen_message
#         }




class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f'chat_{self.room_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        self.delivered = False

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        user = self.scope["user"]

        if not user.is_authenticated:
            # await self.close()
            # print("NOT AUTH")
            return

        text = data['message']
        if not self.delivered:
            self.read = True
            delivered = True
            read = False
        else:
            delivered = False
            read = True

        message = await self.save_message(self.room_id, user.id, text, delivered, read)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event['message']))

    @database_sync_to_async
    def save_message(self, room_id, sender_id, text, delivered, read):
        room = Room.objects.get(id=room_id)
        sender = User.objects.get(id=sender_id)
        message = Message.objects.create(
            room=room, 
            sender=sender, 
            text=text, 
            delivered=delivered, 
            read=read
        )
        return {
            'id': message.id,
            'user_id': str(sender.id),
            'sender': sender.username,
            'text': message.text,
            'timestamp': str(message.timestamp),
            'delivered': message.delivered,
            'read': message.read
        }
