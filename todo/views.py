from django.shortcuts import render

from rest_framework.generics import (
	ListAPIView,
	CreateAPIView,
	DestroyAPIView,
	UpdateAPIView
	)
from .serializers import TodoSerializer

from .models import Todo

# Create your views here.


class ListTodoAPIView(ListAPIView):
	"""This endpoint lists all the available todos from the database."""
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class CreateTodoAPIView(CreateAPIView):
	"""This endpoint allows for the creation of a new todo item."""
	queryset = Todo.objects.all()
	serializer_class = TodoSerializer


class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for the update of a particular todo item 
    by passing the id of that todo item."""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for the deletion of a 
    particular todo item from the database."""
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
