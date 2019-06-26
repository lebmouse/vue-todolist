from django.shortcuts import render
from django.views.generic import ListView

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer
# Create your views here.


class TodoLV(ListView):
    model = Todo
    context_object_name = 'todos'
    template_name = "index.html"


class TodoList(APIView):
    def get(self, request, format=None):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    def get(self, request, todo_id, format=None):
        todo = Todo.objects.get(id=todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def delete(self, request, todo_id, format=None):
        todo = Todo.objects.get(id=todo_id)
        if todo is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, todo_id, format=None):
        todo = Todo.objects.get(id=todo_id)
        if todo is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
