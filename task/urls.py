from rest_framework.routers import DefaultRouter 
from django.urls import path, include
from .views import TaskViewSet
router = DefaultRouter()
router.register('router', TaskViewSet, basename='router')

urlpatterns = [
    path('', include(router.urls)),
]
