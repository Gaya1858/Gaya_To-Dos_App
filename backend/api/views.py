from django.shortcuts import render
from rest_framework import generics , permissions # import DRF's generics class of views
from .serializers import TodoSerializer
from todo.models import Todo


""" Create your views here.
    we create todolist that uses generics.ListAPIView. it is built in generic class which
    creates a read-only endpoint for model instances. 
     # ListAPIView requires two mandatory attributes, serializer_class and queryset
    # We specify TodoSperializer which we have earlier implemented 
"""

class TodoList(generics.ListAPIView):

    serializer_class = TodoSerializer

    """
        get_queryset returns the querydet of todo objects for the view
    """
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')

class TodoListCreate(generics.ListCreateAPIView):

    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    """
        get_queryset returns the querydet of todo objects for the view
    """
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
