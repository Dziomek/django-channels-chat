from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('chat/<str:username>/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]

