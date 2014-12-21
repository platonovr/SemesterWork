from django.conf.urls import url, patterns
from django.views.generic import ListView, DetailView
from JobApp.models import Task, Goal, Bill


urlpatterns = patterns('',
                       url(r'^tasks/', ListView.as_view(model=Task, template_name="JobApp/task_list.html"),
                           name='tasks'),
                       url(r'task_details/(?P<pk>\d+)/$',
                           DetailView.as_view(model=Task, template_name="JobApp/task_details.html"),
                           name='task_details'),
                       url(r'^goals/', ListView.as_view(model=Goal, template_name="JobApp/goal_list.html"),
                           name='goals'),
                       url(r'^bills/', ListView.as_view(model=Bill, template_name="JobApp/bill_list.html"),
                           name='bills'),
                       url(r'^task_form/$', 'JobApp.views.task_form', name='task_form'),

)