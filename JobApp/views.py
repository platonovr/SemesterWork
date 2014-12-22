from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Q, F
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from JobApp.forms import TaskForm
from JobApp.models import Task


@login_required(login_url=reverse_lazy("sign_in"))
def task_form(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('job:tasks'))
    else:
        form = TaskForm()
        return render(request, 'JobApp/task_form.html', {'form': form})


def tasks(request):
    global task_list
    search_string = request.GET.get("search_string")
    show_light = request.GET.get("priority")
    if search_string:
        search_string = str(search_string)
        task_list = Task.objects.filter(
            Q(name__contains=search_string) | Q(description__contains=search_string))
    elif show_light:
        task_list = Task.objects.filter(critical_hours__lt=F('hours'))
    else:
        task_list = Task.objects.all()
    return render(request, 'JobApp/task_list.html', {"task_list": task_list})