from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from excercise.views import custom_login, custom_logout
from django.conf.urls.static import static
from django.conf import settings
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^assignments/', include('excercise.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  custom_login),
    url(r'^accounts/logout/$', custom_logout ),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
