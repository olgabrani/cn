from django.contrib import admin
from django.contrib.auth.models import User
from excercise.models import Course, Exercise, Question, Submission, Application, Grade, Answer
from parsing.models import Parse

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'examiner', 'grade' )

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')

class QuestionInline(admin.StackedInline):
    model = Question


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number','is_active', 'course')
    inlines = [
        QuestionInline
    ]

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'student','state', 'grade', 'examiner', 'datetime_submitted', 'datetime_corrected',)

admin.site.register(Application)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Answer)
