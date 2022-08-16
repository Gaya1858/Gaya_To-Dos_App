from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import generics, permissions  # import DRF's generics class of views
from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo
from django.db import InternalError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)


class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed = not serializer.instance.completed
        serializer.save()


"""
    @csrf_exempt,  becuase the post request is coming from a different domain(the frontend domain)
    and will not have the token required to pass the CSRF checks (Cross Site Request Forgery), 
    we use csrf_exempt for this view.
"""


@csrf_exempt
def signup(request):
    # we check the request was aperformed using the HTTP 'POST'
    if request.method == 'POST':
        try:
            data = JSONParser().parse(
                request)  # JSON parse() to parse the JSON request content and return data as a dictionary
            user = User.objects.create_user(username=data['username'], password=data['password'])
            user.save()  # save the user object to the database

            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except InternalError:
            return JsonResponse({'error': "username taken . choose another username"}, status=400)


@csrf_exempt
def login(request):
    # we check the request was aperformed using the HTTP 'POST'
    if request.method == 'POST':
        data = JSONParser().parse(
            request)  # JSON parse() to parse the JSON request content and return data as a dictionary
        user = authenticate(request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': "unable to login. check username and password"}, status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
