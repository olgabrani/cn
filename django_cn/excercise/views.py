from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from excercise.models import Course, Exercise

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    courses = Course.objects.all()

    return render_to_response('index.html',{'courses':courses}, context)

def course(request, course_code):

    context = RequestContext(request)
    course = Course.objects.get(code=course_code)

    return render_to_response('course.html',{'course':course}, context)

def exercise(request, course_code, exercise_number):

    context = RequestContext(request)
    course = Course.objects.get(code=course_code)
    exercise = Exercise.objects.get(course=course,number=exercise_number)
    print '!!!', exercise
    return render_to_response('exercise.html',{'course':course, 'exercise':exercise}, context)

