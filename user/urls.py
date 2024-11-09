from django.urls import path, include
from .views import  UserCreateApi, protectedview

urlpatterns = [
    path('create', UserCreateApi),
    path('protected', protectedview),
]
