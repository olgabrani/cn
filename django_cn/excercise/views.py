from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from excercise.models import Course, Exercise, MdlUser, MdlCourse, MdlUserEnrolments, ProxyUser
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate, login
from django.conf import settings

def is_examiner(user):
    # Can be used as a decoreator @user_passes_test(is_examiner)
    return user.groups.filter(name='examiner')


@login_required
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    courses = Course.objects.all()
    mdlusers = MdlUser.objects.using('users').all()
    mdlcourses = MdlCourse.objects.using('users').all()
    enrolments = MdlUserEnrolments.objects.using('users').all()
    proxyUser = ProxyUser.objects.get(pk=request.user.pk)

    return render_to_response('index.html',{'courses':courses, 'users':mdlusers, 'mdlcourses':mdlcourses, 'enrolments':enrolments,'proxyUser':proxyUser
    }, context)


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

@login_required
@user_passes_test(is_examiner)
def examiner_index(request):
    
    context = RequestContext(request)

    return render_to_response('examiner/index.html', context)


def custom_login(request):
    context = RequestContext(request)
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            if is_examiner(user):
                return HttpResponseRedirect(settings.EXAMINER_LOGIN_REDIRECT_URL)
            else:
                return HttpResponseRedirect(settings.USER_LOGIN_REDIRECT_URL)
        else:
            print 'skata'
    else:
        return render_to_response('registration/login.html', {}, context)

@login_required
def custom_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/accounts/login')
