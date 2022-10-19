from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>', views.room, name='room'),
    path('rooms/create', views.create_room, name='create_room'),
    path('join/<str:room_name>', views.enter_room_password, name='enter_room_password'),
    path('join_entered/<str:room_name>', views.join_room, name='join_room'),
    path('delete_room/<str:room_name>', views.delete_room, name='delete_room')
]