# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from excercise.models import Course, Exercise, MdlUser, MdlCourse, MdlUserEnrolments, ProxyUser, Submission
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import login, logout
from django.contrib.auth import authenticate, login
from django.conf import settings
from excercise.forms import SubmissionForm

def is_examiner(user):
    # Can be used as a decoreator @user_passes_test(is_examiner)
    return user.groups.filter(name='examiner')


@login_required
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)
    has_course_link = True
    courses = Course.objects.all().select_related()
    res = []
    for c in courses:
        try:
            c.group_name = c.get_group(request.proxyUser).name
        except:
            c.group_name = None
        for e in c.exercises:
            e.submission_state = e.submission_state(request.proxyUser)
            e.has_submission_link = False
            has_link = [u'Ημιτελής', u'Ανοιχτή']
            if e.submission_state in has_link: 
                e.has_submission_link = True
            res.append({'course_code': c.code, 'title':e.title, 'number':e.number, 'submission_state':e.submission_state, 'has_submission_link':e.has_submission_link})
    return render_to_response('index.html',{'has_course_link':has_course_link, 'exercises':res, 'courses': courses,}, context)

@login_required
def student_redir(request):
     return redirect('index')

@login_required
def course(request, course_code):

    context = RequestContext(request)
    course = Course.objects.get(code=course_code)
    try: 
        course.group_name = course.get_group(request.proxyUser).name
    except:
        course.group_name = None
    exercises = course.exercises
    for e in exercises:
        e.submission_state = e.submission_state(request.proxyUser)
        e.submission_code = e.submission_code(request.proxyUser)
        e.has_submission_link = False
        has_link = [u'Ημιτελής', u'Ανοιχτή']
        if e.submission_state in has_link: 
            e.has_submission_link = True
    return render_to_response('course.html',{'course':course, 'exercises':exercises }, context)



@login_required
def exercise(request, course_code, exercise_number):

    if request.method == 'POST':
        submission_code = request.POST.get('submission_code', 'O')
        print submission_code
        return redirect('index')
    context = RequestContext(request)
    course = Course.objects.get(code=course_code)
    try:
        course.group = course.get_group(request.proxyUser).name
    except:
        course.group = None
    exercise = Exercise.objects.get(course=course,number=exercise_number)
    exercise.submission_code = exercise.submission_code(request.proxyUser)


    return render_to_response('exercise.html',{'course':course, 'exercise':exercise}, context)

def custom_login(request):
    context = RequestContext(request)
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    error = ''
    if user is not None:
        if user.is_active:
            login(request, user)
            if is_examiner(user):
                return HttpResponseRedirect(settings.EXAMINER_LOGIN_REDIRECT_URL)
            else:
                return HttpResponseRedirect(settings.USER_LOGIN_REDIRECT_URL)
        else:
            print 'error'
    else:
        if request.method =='POST':
            error = 'You have an error in your username/password combination or you are not registered to moodle'
        return render_to_response('registration/login.html', {'error':error}, context)


@login_required
def custom_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return HttpResponseRedirect('/accounts/login')

@login_required
@user_passes_test(is_examiner)
def examiner_index(request):
    
    context = RequestContext(request)

    return render_to_response('examiner/index.html', context)

@login_required
@user_passes_test(is_examiner)
def grading_list(request, course_code, exercise_number=None, group_id=None):
    
    submissions = Submission.objects.filter(state='S').select_related()
    if exercise_number:
        submissions = submissions.filter(exercise__number = exercise_number)
    res = []
    for s in submissions:
        exercise_number = s.exercise.number
        exercise_id = s.exercise.pk
        username = s.student.username
        user_id = s.student.pk
        date_modified = s.date_modified
        grade = s.grade
        group = Course.objects.get(code=course_code).get_group(s.student)
        group_name = group.name
        group_pk = group.pk
        res.append({
            'exercise_number': exercise_number,
            'exercise_id': exercise_id,
            'username': username,
            'user_id': user_id,
            'date_modified': date_modified,
            'grade': grade,
            'group_name': group_name,
            'group_pk': group_pk,
        })
    filtering = request.GET.get('filtering')
    context = RequestContext(request)
    my_dict = { 'course_code': course_code,
                'exercise_number': exercise_number,
                'filtering': filtering,
                'res': res,
              }
    return render_to_response('examiner/list.html', my_dict, context)

@login_required
@user_passes_test(is_examiner)
def answer(request, exercise_id, user_id):

    context = RequestContext(request)
    exercise = Exercise.objects.get(pk=exercise_id)
    submission = Submission.objects.get(exercise__pk=exercise_id, student__pk=user_id)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect('examiner_index')
    else:
        form = SubmissionForm(instance=submission)
    my_dict = {
        'exercise': exercise,
        'submission': submission,
        'form': form,
    }
    return render_to_response('examiner/exercise.html', my_dict , context)

