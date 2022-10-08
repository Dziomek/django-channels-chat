from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.start_route),
    path('signin', views.sign_in, name='sign_in'),
    path('signup', views.sign_up, name='sign_up'),
    path('logout', views.logout, name='logout'),
]