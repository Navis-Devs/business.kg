from django.urls import path

from .views import (
    RoomListView,
    RoomDeleteView,
    ChatGetView,
    RoomCreateView,
)

urlpatterns = [
    path('chat-list/', RoomListView.as_view()),
    path('chat-delete/<int:id>', RoomDeleteView.as_view()),
    path('chat/<int:chat_id>', ChatGetView.as_view()),
    path('chat-create/', RoomCreateView.as_view()),
]