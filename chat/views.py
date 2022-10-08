from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Room, Message


@login_required
def rooms(request):
    room_objects = Room.objects.all()

    return render(request, 'chat/rooms.html', {'rooms': room_objects})


@login_required
def room(request, slug):
    room_object = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room_object)

    return render(request, 'chat/room.html', {'room': room_object, 'messages': messages})

