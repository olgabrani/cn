from django.forms import ModelForm
from excercise.models import Submission
from django.forms.formsets import formset_factory

class SubmissionForm(ModelForm):
    
    class Meta:
        model = Submission
        fields = ['grade']

SubmissionFormSet = formset_factory(SubmissionForm)
