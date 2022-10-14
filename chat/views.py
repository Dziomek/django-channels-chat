from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
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


@login_required
def create_room(request):
    if request.method == 'POST':
        room_name = request.POST['room_name']
        password = request.POST['password']
        room_object = Room(name=room_name, password=password, admin=request.user)
        room_object.save()

    return redirect('rooms')



