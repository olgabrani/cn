import re, os, sys
from os.path import join
from django.contrib import admin
from django.conf import settings
from models import Parse
from excercise.models import Question, Exercise

class ParseAdmin(admin.ModelAdmin):
    list_display = ('name', 'exercise')
    def save_model(self, request, obj, form, change):
        exercise_id = obj.exercise.pk
        print exercise_id
        try:
            # get file path
            f_path = os.path.join(settings.BASE_DIR, obj.document.path)
            # open file
            f = open(f_path)
            arr = []
            for line in f:
                u = line.decode("utf-8-sig")
                line = u.encode("utf-8")
                res = re.split('\t', line)
                
                if len(res) > 1:
                    d = {}
                    d['num'] = res[0]
                    d['text'] = res[1]
                    arr.append(d)
                else:
                    d = arr[-1]
                    d['text'] = d['text'] + res[0]
           
            # if flag purge is True, delete all questions associated with this exercise
            if obj.purge == True:
                questions = Question.objects.filter(exercise_id=exercise_id)
                questions.delete()
            
            #import new questions 
            for a in arr:
               q = Question.objects.create(exercise_id=exercise_id, order=a['num'], text=a['text'])

            f.close()
            obj.save()

        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except:
            print "Unexpected error:", sys.exc_info()[0]


admin.site.register(Parse, ParseAdmin)
# Register your models here.