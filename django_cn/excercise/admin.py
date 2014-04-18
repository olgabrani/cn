from django.contrib import admin
from excercise.models import Course, Exercise, Question
from django.contrib.auth.models import User


class QuestionInline(admin.StackedInline):
    model = Question

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number','is_active', 'course')
    inlines = [
        QuestionInline
    ]

admin.site.register(Course)
admin.site.register(Exercise, ExerciseAdmin)
