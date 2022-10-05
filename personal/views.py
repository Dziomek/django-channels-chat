from django.shortcuts import render

# Create your views here.
from .models import Message


def home_view(request):
    messages = Message.objects.all()

    return render(request, 'personal/home.html', {'messages': messages})

