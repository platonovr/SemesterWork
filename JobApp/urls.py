from django.conf.urls import url, patterns
from django.views.generic import ListView
from JobApp.models import Task


urlpatterns = patterns('',
                       url(r'^tasks/', ListView.as_view(model=Task, template_name="JobApp/task_list.html"),
                           name='tasks'),

)