from django.contrib import admin
from excercise.models import Course, Exercise, Question, Submission
from django.contrib.auth.models import User


class QuestionInline(admin.StackedInline):
    model = Question

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number','is_active', 'course')
    inlines = [
        QuestionInline
    ]
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'student','state', 'grade')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')

admin.site.register(Course, CourseAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Exercise, ExerciseAdmin)
