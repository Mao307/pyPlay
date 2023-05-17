from django.views.generic import ListView
from .models import TodoList


class ListListView(ListView):
    model = TodoList
    template_name = "todo_app/index.html"
    
