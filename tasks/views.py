from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from tasks.forms import TaskCreateForm, TaskUpdateForm
from tasks.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 15


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("tasks:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("tasks:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:task-list")


def task_status_update(request: HttpRequest, pk=int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("tasks:task-list")
