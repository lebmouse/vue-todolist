from django.shortcuts import render
from django.views.generic import ListView

from .models import Todo
# Create your views here.


class TodoLV(ListView):
  model = Todo
  context_object_name = 'todos'
  template_name = "index.html"
  