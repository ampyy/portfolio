from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", home, name='home'),
    path("post-detail/<int:pk>", post, name='post-detail'),
]
