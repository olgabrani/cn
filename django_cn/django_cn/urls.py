from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from excercise.views import custom_login, custom_logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_cn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^excercise/', include('excercise.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  custom_login),
    url(r'^accounts/logout/$', custom_logout ),
)
