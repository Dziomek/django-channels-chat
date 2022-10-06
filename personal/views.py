from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from annoying.functions import get_object_or_None

# Create your views here.
from .models import Message, Room


def username_and_room(request):
    if request.method == 'POST':
        username = request.POST['username']
        room_name = request.POST['room_name']

        if username and room_name:

            room = get_object_or_None(Room, room_name=room_name)
            if not room:
                new_room = Room.objects.create(room_name=room_name)
                new_room.save()

            return redirect('chat', username=username, room_name=room_name)

    return render(request, 'personal/start_page.html')


def chat(request, username, room_name):
    messages = Message.objects.filter(room_name=room_name)

    return render(request, 'personal/home_page.html', {'messages': messages,
                                                       'username': username,
                                                       'room_name': room_name})

