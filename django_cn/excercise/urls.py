from django.conf.urls import patterns,url
from excercise import views
from django.views.generic.base import RedirectView
from django.shortcuts import redirect
from excercise.views import AnswerPDFView, AnswersPDFView

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^course/(?P<course_code>\w+)/$', views.course, name='course'),
        url(r'^course/(?P<course_code>\w+)/(?P<exercise_number>\d+)/?$', views.exercise, name='exercise'),
        url(r'^course/$', views.student_redir, name='student_redir'),
        url(r'^grades/$', views.grades, name='grades'),
        url(r'^examiner/$', views.examiner_index, name='examiner_index'),
        url(r'^examiner/(?P<course_code>\w+)/$', views.grading_list, name='grading_list'),
        url(r'^examiner/(?P<course_code>\w+)/(?P<exercise_number>\d+)/?$', views.grading_list, name='grading_list'),
        url(r'^examiner/(?P<course_code>\w+)/(?P<exercise_number>\d+)/(?P<group_id>\d+)/?$', views.grading_list, name='grading_list'),
        url(r'^answer/(?P<exercise_id>\d+)/(?P<user_id>\d+)/?$', views.answer, name='answer'),
        url(r'^pdf-answer/(?P<exercise_id>\d+)/(?P<user_id>\d+)/?$', AnswerPDFView.as_view(), name='pdf_answer'),
        url(r'^pdf-answers/$', views.answers_view, name='pdf_answers'),
        url(r'^delete_image/$', views.delete_image, name='delete_image'),
        url(r'^set_suggested_answer/$', views.set_suggested_answer, name='set_suggested_answer'),
    )
