from django.forms import ModelForm
from excercise.models import Submission

class SubmissionForm(ModelForm):
    
    class Meta:
        model = Submission
        fields = ['grade']
