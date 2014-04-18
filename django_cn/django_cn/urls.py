from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_cn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^excercise/', include('excercise.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout, {'next_page': '/excercise/'}),
)
