from django.forms import ModelForm
from excercise.models import Submission
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory

class SubmissionForm(ModelForm):
    
    class Meta:
        model = Submission
        fields = ['grade']

SubmissionFormSet = modelformset_factory(Submission, form=SubmissionForm, extra=0)

class StudentSubmissionForm(ModelForm):
    
    class Meta:
        model = Submission
        fields = []
