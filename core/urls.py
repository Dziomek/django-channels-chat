from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.start_route),
    path('signin', views.sign_in, name='sign_in'),
    path('rooms', views.rooms, name='rooms'),
    path('signup', views.sign_up, name='sign_up'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]