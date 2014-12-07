from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from JobApp.forms import TaskForm


def task_form(request):
    if request.POST:
        form = TaskForm(request.POST)
        if form.is_valid():
            if request.is_ajax():
                pass
            pass
        pass
    else:
        form = TaskForm()
        return render(request, 'JobApp/task_form.html', {'form': form})