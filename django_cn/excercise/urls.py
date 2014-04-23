from django.conf.urls import patterns,url
from excercise import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^course/(?P<course_code>\w+)/$', views.course, name='course'),
        url(r'^course/(?P<course_code>\w+)/(?P<exercise_number>\d+)/?$', views.exercise, name='exercise'),
        url(r'^examiner/$', views.examiner_index, name='examiner_index'),
    )
