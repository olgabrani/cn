from django.conf.urls import patterns,url
from excercise import views
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from excercise.views import HelloPDFView

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^foo/$', HelloPDFView.as_view(), name='foo'),
        url(r'^course/(?P<course_code>\w+)/$', views.course, name='course'),
        url(r'^course/(?P<course_code>\w+)/(?P<exercise_number>\d+)/?$', views.exercise, name='exercise'),
        url(r'^course/$', views.student_redir, name='student_redir'),
        url(r'^examiner/$', views.examiner_index, name='examiner_index'),
        url(r'^examiner/(?P<course_code>\w+)/$', views.grading_list, name='grading_list'),
        url(r'^examiner/(?P<course_code>\w+)/(?P<exercise_number>\d+)/?$', views.grading_list, name='grading_list'),
        url(r'^examiner/(?P<course_code>\w+)/(?P<exercise_number>\d+)/(?P<group_id>\d+)/?$', views.grading_list, name='grading_list'),
        url(r'^answer/(?P<exercise_id>\d+)/(?P<user_id>\d+)/?$', views.answer, name='answer'),
    )
