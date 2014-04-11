from django.conf.urls import patterns,url
from cn import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'))
