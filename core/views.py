from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from annoying.functions import get_object_or_None
from .models import Message, Room
from .forms import SignUpForm


def start_route(request):
    return redirect('sign_in')


@login_required(login_url='sign_in')
def rooms(request):
    return render(request, 'core/rooms.html')


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('rooms')

    return render(request, 'core/start_page.html')


def logout(request):
    auth.logout(request)
    return redirect('sign_in')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print('siemano')
            login(request, user)

            return redirect('rooms')
        else:
            form = SignUpForm()
    return redirect('sign_in')


def chat(request, username, room_name):
    messages = Message.objects.filter(room_name=room_name)

    return render(request, 'core/room_page.html', {'messages': messages,
                                                       'username': username,
                                                       'room_name': room_name})

