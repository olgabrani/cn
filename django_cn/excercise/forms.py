from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from excercise.models import Submission, Answer, Grade

class SubmissionForm(ModelForm):
    
    class Meta:
        model = Submission
        fields = ['grade']

SubmissionFormSet = modelformset_factory(Submission, form=SubmissionForm, extra=0)

class GradeForm(ModelForm):
    
    class Meta:
        model = Grade
        exclude = ['course', 'student']

GradeFormSet = modelformset_factory(Grade, form=GradeForm, extra=0)



class AnswerTextForm(ModelForm):
    
    class Meta:
        model = Answer
        fields = ['question', 'student', 'answer']

class AnswerImageForm(ModelForm):
    
    class Meta:
        model = Answer
        fields = ['question', 'student', 'img']

class StudentSubmissionForm(ModelForm):
    
    class Meta:
        model = Submission
        fields = []
