from django.conf.urls import patterns, include, url
from project import views
import settings

from django.contrib import admin
admin.autodiscover()
                                                                                                               
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Q_manage_s.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^personal_homepage/$', views.personal_homepage,name="homepage"),
    #(r'^detail/(\d+)/$',views.detail),
    url(r'^changedesign/', views.changedesign,name="design_change"),
    url(r'^delayproject/$', views.delayproject,name="project_delay"),
    url(r'^pauseproject-(?P<id>\d+)/$', views.pauseproject,name="project_pause"),
    url(r'^deleteproject-(?P<id>\d+)/$', views.deleteproject,name="project_delete"),
    url(r'^projectid/', views.project,name="project"),

   )