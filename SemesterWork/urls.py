from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import DetailView, ListView
from EventApp.models import Event
from EventApp.views import PlaceListView, TypeListView
from SemesterWork import settings

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
                       url(r'^places/', PlaceListView.as_view(), name='places'),
                       url(r'^create_place/', 'EventApp.views.create_place', name='create_place'),
                       url(r'^types/', TypeListView.as_view(), name='types'),
                       url(r'^create_type/', 'EventApp.views.create_type', name='create_type'),
                       url(r'^go/$', 'EventApp.views.go', name='go'),
                       url(r'^registraion/', 'EventApp.views.registration', name='registration'),
                       url(r'^changepswd/', 'EventApp.views.change_password', name='change_password'),
)

urlpatterns += patterns('',
                        url(r'^media/(?P<path>.*)', 'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}),
)

