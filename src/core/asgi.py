import os
from django.core.asgi import get_asgi_application
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from apps.chat.middleware import TokenAuthMiddleware
from channels.auth import AuthMiddlewareStack
from apps.chat.consumers import ChatConsumer
from django.urls import path, re_path


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django_asgi_app = get_asgi_application()


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_id>\d+)/$', ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    "http": django_asgi_app, 
    "websocket": TokenAuthMiddleware(
        URLRouter(websocket_urlpatterns)
    ),
})
