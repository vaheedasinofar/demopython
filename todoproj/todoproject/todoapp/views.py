import task1 as task1
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from todoapp.forms import TodoForm
from todoapp.models import Task
from django.views.generic import ListView, UpdateView
from django.views.generic.detail import DetailView


class Tasklistview(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'


class Taskdetailview(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('dbvhome', kwargs={'pk': self.object.id})


def index(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, priority=priority, date=date)
        task.save()

    return render(request, "index.html", {'task1': task1})


def delete(request, taskid):
    tas = Task.objects.get(id=taskid)
    if request.method == 'POST':
        tas.delete()
        return redirect('/')
    return render(request, "delete.html")


def update(request, id):
    task = Task.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, "edit.html", {'f': f, 'task': task})
