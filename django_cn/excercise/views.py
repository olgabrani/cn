# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import login, logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from excercise.forms import SubmissionForm, SubmissionFormSet, StudentSubmissionForm, AnswerTextForm, AnswerImageForm
from excercise.models import Course, Exercise, MdlUser, MdlCourse, MdlUserEnrolments, ProxyUser, Submission, Answer, Question
from excercise.models import submission_list
from easy_pdf.views import PDFTemplateView
from easy_pdf.rendering import render_to_pdf_response

def is_examiner(user):
    # Can be used as a decoreator @user_passes_test(is_examiner)
    return user.groups.filter(name='examiner')

def slicedict(d, s):
    return {k:v for k,v in d.iteritems() if k.startswith(s)}

@login_required
def index(request):
    context = RequestContext(request)
    has_course_link = True
    courses = Course.objects.filter(is_active=True).select_related()
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
            res.append({'course_code': c.code, 
                        'title':e.title, 
                        'number':e.number, 
                        'submission_state':e.submission_state, 
                        'has_submission_link':e.has_submission_link, 
                        'document':e.document})
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

    context = RequestContext(request)
    course = Course.objects.get(code=course_code)
   
    try:
        course.group = course.get_group(request.proxyUser).name
    except:
        course.group = None
    
    exercise = Exercise.objects.select_related('questions').get(course=course,number=exercise_number)
    questions = exercise.questions
    student = request.user
    
    try:
        submission = Submission.objects.get(exercise=exercise,student=student)
        if request.method == 'POST':
            form = StudentSubmissionForm(request.POST, instance=submission)
            if form.is_valid():
                new_submission = form.save(commit=False)
    except:
        if request.method == 'POST':
            form = StudentSubmissionForm(request.POST)
            if form.is_valid():
                new_submission = form.save(commit=False)
                new_submission.student = student
                new_submission.exercise = exercise
    
    if request.method == 'POST':
        q_dict = slicedict(request.POST, 'q-')
        for k, v in q_dict.iteritems():
            answer = v
            t = k.split('-',2)
            question_pk = t[1]
            student_pk = t[2]
            try:
                instance = Answer.objects.get(question_id=question_pk,student_id=student_pk)
                form = AnswerTextForm({'question':question_pk, 'student': student_pk, 'answer': answer}, instance=instance)
            except:
                form = AnswerTextForm({'question':question_pk, 'student': student_pk, 'answer': answer})
            if form.is_valid():
                form.save()
        
        
        qi_dict = slicedict(request.FILES, 'qi-')
        for k, v in qi_dict.iteritems():
            img = v
            t = k.split('-',2)
            question_pk = t[1]
            student_pk = t[2]
            print img, '!!!!!'
            try:
                instance = Answer.objects.get(question_id=question_pk,student_id=student_pk)
                form = AnswerImageForm({'question':question_pk, 'student': student_pk},{'img': img}, instance=instance)
            except:
                form = AnswerImageForm({'question':question_pk, 'student': student_pk}, {'img':img})
            if form.is_valid():
                form.save()



        if 'save' in request.POST.keys():
            new_submission.state = 'I'
            new_submission.save()
        else:
            new_submission.state = 'S'
            new_submission.datetime_submitted = datetime.datetime.now()
            new_submission.save()
            return redirect('index')

    for q in questions:
        if q.answer_type == 'T':
            q.field_name = 'q-%d-%d' %(q.pk, student.pk)
            try:
                obj = Answer.objects.get(question_id=q.pk,student_id=student.pk)
                q.value = obj.answer
            except:
                print 'no obj found'
        if q.answer_type == 'I':
            q.field_name = 'qi-%d-%d' %(q.pk, student.pk)
            try:
                obj = Answer.objects.get(question_id=q.pk,student_id=student.pk)
                q.img = obj.img
            except:
                print 'no obj found'

    exercise.submission_code = exercise.submission_code(request.proxyUser)
    my_dict = {'course': course,
               'exercise': exercise,
               'questions': questions, 
    }


    return render_to_response('exercise.html', my_dict, context)

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
    courses = request.proxyUser.enrolled_courses_examiner
    res = []
    for c in courses:
        c.groups = c.get_groups
        for g in c.groups:
            group_id = int(g.id)
            g.cnt_s = submission_list(c.code, None, group_id).count()
            g.cnt_c = submission_list(c.code, None, group_id, "corrected").count()
        for e in c.exercises: 
            e.group_list = []
            e.groups = c.groups
            for g in e.groups:
                group_id = int(g.id)
                cnt_s = submission_list(c.code, e.number, group_id).count()
                cnt_c = submission_list(c.code, e.number, group_id, "corrected").count()
                e.group_list.append({'group_id':group_id, 'cnt_c':cnt_c, 'cnt_s':cnt_s})
            e.cnt_s = e.cnt_submissions()
            e.cnt_c = e.cnt_submissions(filtering='corrected')
            res.append({'course_code': c.code, 
                        'title':e.title, 
                        'number':e.number,
                        'cnt_s':e.cnt_s, 
                        'cnt_c':e.cnt_c, 
                        'groups': e.groups, 
                        'group_list': e.group_list,
                        'document':e.document
                        })
    return render_to_response('examiner/index.html',{ 'exercises':res, 'courses': courses,}, context)

@login_required
@user_passes_test(is_examiner)
def grades(request):
    
    context = RequestContext(request)
    courses = request.proxyUser.enrolled_courses_examiner
    for c in courses:
        c.students = []
        for s in c.student_list: 
            username = s.username
            if c.get_group(s):
                group = c.get_group(s).name
            else:
                None
            exercises = []
            for e in c.exercises:
                try: 
                    e.grade = Submission.objects.get(exercise=e,student=s).grade
                except:
                    e.grade = ''
                exercises.append({
                    'number': e.number,
                    'grade': e.grade,
                })
            c.students.append({
                'username': username,
                'group': group,
                'exercises': exercises,
            })

    return render_to_response('examiner/grades.html',{'courses': courses,}, context)



@login_required
@user_passes_test(is_examiner)
def grading_list(request, course_code, exercise_number=None, group_id=None):
    
    filtering = request.GET.get('filtering', None)
    submissions = submission_list(course_code, exercise_number, group_id, filtering)
    
    if request.method == 'POST':
        formset = SubmissionFormSet(request.POST, queryset=submissions)
        if formset.is_valid():
            for f in formset:
                s = f.save(commit=False)
                if s.grade:
                    s.state = 'C'
                    s.datetime_corrected = datetime.datetime.now()
                else:
                    s.state = 'S'
                s.save()
                return redirect('examiner_index')
    else:
        formset = SubmissionFormSet(queryset=submissions)
    res = []
    i = 0
    
   
    for s in submissions:
        group = Course.objects.get(code=course_code).get_group(s.student)
        if group:
            group_name = group.name
            group_pk = group.pk
        else:
            group_name = None
            group_pk = None
        res.append({
            'exercise_number': s.exercise.number,
            'exercise_id': s.exercise.pk,
            'username': s.student.username,
            'user_id': s.student.pk,
            'grade': s.grade,
            'group_name': group_name,
            'group_pk': group_pk,
            'datetime_submitted': s.datetime_submitted,
        })
    
    for f in formset:
        f.exercise_number = res[i].get('exercise_number')
        f.exercise_id = res[i].get('exercise_id')
        f.username = res[i].get('username')
        f.user_id = res[i].get('user_id')
        f.group_name = res[i].get('group_name')
        f.group_pk = res[i].get('group_pk')
        f.datetime_submitted = res[i].get('datetime_submitted')
        f.hidden_input = 'a-%d-%d' %(res[i].get('exercise_id'), res[i].get('user_id'))
        i=i+1
    
    context = RequestContext(request)
    my_dict = { 'course_code': course_code,
                'exercise_number': exercise_number,
                'filtering': filtering,
                'res': res,
                'formset':formset,
              }
    return render_to_response('examiner/list.html', my_dict, context)

@login_required
@user_passes_test(is_examiner)
def answer(request, exercise_id, user_id):

    context = RequestContext(request)
    exercise = Exercise.objects.get(pk=exercise_id)
    student = User.objects.get(pk=user_id)
    submission = Submission.objects.get(exercise__pk=exercise_id, student__pk=user_id)
    
    try:
        course.group = exercise.course.get_group(student).name
    except:
        course.group = None
    
    questions = exercise.questions
    for q in questions:
        try:
            obj = Answer.objects.get(question_id=q.pk,student_id=student.pk)
            q.answer = obj.answer
            q.img = obj.img
        except:
            q.answer = 'No answer'

    if request.method == 'POST':
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            new_submission = form.save(commit=False)
            grade = request.POST.get('grade', None)
            if grade:
                new_submission.datetime_corrected = datetime.datetime.now()
                new_submission.state = 'C'
            else:
                new_submission.state = 'S'
            new_submission.save()
            return redirect('examiner_index')
    else:
        form = SubmissionForm(instance=submission)
    my_dict = {
        'exercise': exercise,
        'questions': questions,
        'submission': submission,
        'form': form,
        'student': student,
        'group': course.group,
    }
    return render_to_response('examiner/exercise.html', my_dict , context)

class AnswerPDFView(PDFTemplateView):
    template_name = "pdf_answer.html"
    
    def get_context_data(self, **kwargs):
        context = super(AnswerPDFView, self).get_context_data(**kwargs)
        user_id = context['user_id']
        exercise_id = context['exercise_id']
        
        exercise = Exercise.objects.get(pk=exercise_id)
        student = User.objects.get(pk=user_id)
    
        submission = Submission.objects.get(exercise=exercise,student=student)
        try:
            course.group = exercise.course.get_group(student).name
        except:
            course.group = None
    
        questions = exercise.questions
        for q in questions:
            try:
                obj = Answer.objects.get(question_id=q.pk,student_id=student.pk)
                q.answer = obj.answer
                q.img = obj.img
            except:
                q.answer = 'No answer'
                q.img = False
    
        res = []
        res.append({
            'exercise': exercise,
            'questions': questions,
            'student': student,
            'group': course.group,
            'submission': submission,
        })
        return super(AnswerPDFView, self).get_context_data(
            pagesize="A4",
            title="Hi there!",
            res=res,
            **kwargs
        )

class AnswersPDFView(PDFTemplateView):
    template_name = "pdf_answer.html"

    def get_context_data(self, **kwargs):
        if request.POST:
            res = request.POST['checks']
        else: 
            res = 'skata'
        return super(AnswersPDFView, self).get_context_data(
            pagesize="A4",
            title="Hi there!",
            res=res,
            **kwargs
        )

@login_required
@user_passes_test(is_examiner)
def answers_view(request):
    
    context = RequestContext(request)
    checks = request.POST
    a_dict = slicedict(request.POST, 'a-')
    res = []
    for k, v in a_dict.iteritems():
        if v == 'checked':
            t = k.split('-',2)
            exercise_id = t[1]
            user_id = t[2]
            try:
                exercise = Exercise.objects.get(pk=exercise_id)
                student = User.objects.get(pk=user_id)
                print 'student_id', student
            
                submission = Submission.objects.get(exercise=exercise,student=student)
                try:
                    course.group = exercise.course.get_group(student).name
                except:
                    course.group = None
            
                questions = exercise.questions
                for q in questions:
                    try:
                        obj = Answer.objects.get(question_id=q.pk,student_id=student.pk)
                        q.answer = obj.answer
                        q.img = obj.img
                    except:
                        q.answer = 'No answer'
                        q.img = False
            
                res.append({
                    'exercise': exercise,
                    'questions': questions,
                    'student': student,
                    'group': course.group,
                    'submission': submission,
                })
            except:
                print 'error'
    context['res'] = res
    return render_to_pdf_response(request, "pdf_answer.html", context, 'answers', "utf-8")




