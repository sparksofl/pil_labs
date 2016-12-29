from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new$', views.post_create, name='post_new'),
    url(r'^update/(?P<pk>\d+)$', views.post_update, name='post_update'),
    url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='post_delete'),
]
