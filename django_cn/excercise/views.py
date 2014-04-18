from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from excercise.models import Course, Exercise, MdlUser, MdlCourse, MdlUserEnrolments
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

@login_required
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    courses = Course.objects.all()
    mdlusers = MdlUser.objects.using('users').all()
    mdlcourses = MdlCourse.objects.using('users').all()
    enrolments = MdlUserEnrolments.objects.using('users').all()

    return render_to_response('index.html',{'courses':courses, 'users':mdlusers, 'mdlcourses':mdlcourses, 'enrolments':enrolments}, context)


@login_required
def course(request, course_code):

    context = RequestContext(request)
    course = Course.objects.get(code=course_code)

    return render_to_response('course.html',{'course':course}, context)


@login_required
def exercise(request, course_code, exercise_number):

    context = RequestContext(request)
    course = Course.objects.get(code=course_code)
    exercise = Exercise.objects.get(course=course,number=exercise_number)

    return render_to_response('exercise.html',{'course':course, 'exercise':exercise}, context)

