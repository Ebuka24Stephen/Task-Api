from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.throttling import UserRateThrottle

from .models import Task 
from .serializers import TaskSerializer 
from rest_framework.viewsets import ModelViewSet
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = ([IsAuthenticated])
    throttle_classes = [UserRateThrottle]

    def retrieve(self,request, pk):
        task = get_object_or_404(self.queryset, id=pk)
        serializer = self.get_serializer(task)
        return  Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self, request, pk):
        task = get_object_or_404(self.queryset, id=pk)
        serializer = self.get_serializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def destroy(self, request, pk):
        task = get_object_or_404(self.queryset, id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

