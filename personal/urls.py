from django.urls import path
from . import views

urlpatterns = [
    path('', views.username_and_room, name='username_and_room'),
    path('chat/<str:room_name>/user=<str:username>/', views.chat, name='chat'),
]