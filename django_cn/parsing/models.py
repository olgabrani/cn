from django.db import models
from excercise.models import Exercise, Question
from filebrowser.fields import FileBrowseField

class Parse(models.Model):
    exercise = models.ForeignKey(Exercise)
    purge = models.BooleanField(help_text='Deletes all previous questions associated with this exercise', default=False)
    document = FileBrowseField("TXT", max_length=200, directory="txt/", extensions=[".txt",".md"])

    class Meta:
        verbose_name = 'question'

    def name(self):
        return self.document.name

    def __unicode__(self):
        return self.document.name

class Suggested(models.Model):
    exercise = models.ForeignKey(Exercise)
    purge = models.BooleanField(help_text='Deletes all previous answers associated with this exercise', default=False)
    document = FileBrowseField("TXT", max_length=200, directory="txt/", extensions=[".txt",".md"])


    class Meta:
        verbose_name = 'suggested answer'
    
    def name(self):
        return self.document.name

    def __unicode__(self):
        return self.document.name
