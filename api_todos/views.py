from urllib import request
from django.shortcuts import render
from rest_framework.views import (
    APIView
)
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView
)

from rest_framework.permissions import IsAuthenticated,IsAdminUser

from .permissions import IsOwner
from .serializers import TodoSerializer,TagSerializer
from .models import Tag, Todo

class GetAllTodos(ListAPIView) :
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class GetAllTags(ListAPIView) :
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class GetCreateTodos(ListCreateAPIView) :
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated,IsOwner]

    def get_queryset(self):
        user = self.request.user
        if user :
            return Todo.objects.filter(user=user)
        return Todo.objects.none()

class GetUpdateDeleteTodo(RetrieveUpdateDestroyAPIView) :
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated,IsOwner]