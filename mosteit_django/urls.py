from django.conf.urls import patterns, include, url
from django.contrib import admin

from forum import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mosteit_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',              views.index, name='index'),
    url(r'^new_thread/',    views.new_thread,name='new_thread'),
    url(r'^view_thread/',   views.view_thread, name='view_thread'),
    url(r'^delete_thread/', views.delete_thread, name='delete_thread'),
    url(r'^new_post/',      views.new_post, name='new_post'),
    url(r'^delete_post/',   views.delete_post, name='delete_post'),
    url(r'^new_thread_error/', views.new_thread_error, name='new_thread_error'),
    url(r'^admin/', include(admin.site.urls))
)
