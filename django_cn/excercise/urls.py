from django.conf.urls import patterns,url
from excercise import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^course/(?P<course_code>\w+)/$', views.course, name='course'),
        url(r'^course/(?P<course_code>\w+)/(?P<exercise_number>\d+)/?$', views.exercise, name='exercise'),
        url(r'^examiner/$', views.examiner_index, name='examiner_index'),
        url(r'^examiner/(?P<course_code>\w+)/$', views.list_course, name='list_course'),
        url(r'^examiner/(?P<course_code>\w+)/(?P<exercise_number>\d+)/?$', views.list_exercise, name='list_exercise'),
        url(r'^examiner/(?P<course_code>\w+)/(?P<exercise_number>\d+)/(?P<team_id>\d+)/?$', views.list_team, name='list_team'),
        url(r'^examiner/(?P<course_code>\w+)/(?P<exercise_number>\d+)/(?P<team_id>\d+)/(?P<user_id>\d+)/?$', views.answer, name='answer'),
    )
