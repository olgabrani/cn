from django.contrib import admin
from excercise.models import Course, Exercise

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('title', 'number','is_active', 'course')

admin.site.register(Course)
admin.site.register(Exercise, ExerciseAdmin)
