from django.conf.urls import patterns, include, url
#from data.views import index
#from data.views import present_output
from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_web.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^app/$', 'flask_app.controller.index'),
    url(r'^data1/$', 'data.views.index'),
#    url(r'^data1/', 'data.views.index'),
)
