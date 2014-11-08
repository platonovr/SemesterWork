from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView, ListView
from EventApp.models import Event

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'SemesterWork.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^menu/', 'EventApp.views.menu', name='menu'),
                       url(r'^$', 'EventApp.views.sign_in', name='sign_in'),
                       url(r'^events/', 'EventApp.views.events', name='events'),
                       url(r'^create_event/', 'EventApp.views.create_event', name='create_event'),
                       url(r'^event/(?P<pk>\d+)',
                           DetailView.as_view(model=Event, template_name="EventApp/event_details.html"),
                           name='event_details'),
                       url(r'^settings/', 'EventApp.views.settings', name='settings'),
                       url(r'^exit/', 'EventApp.views.exit', name='exit'),
                       url(r'^job/', include('JobApp.urls', namespace='job')),
)
