from django import forms
form excericse import Submission

class SubmissionForm(forms.ModelForm):
    
    class Meta:
        model = Submission
        fields = ('state',)
