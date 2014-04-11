from django.db import models

class Course(models.Model):

    SEMESTER = (
        ('S', 'Summer'),
        ('W', 'Winter'),
    ) 
    
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=64)
    year = models.CharField(max_length=128)
    semester = models.CharField(max_length=1,choices=SEMESTER)

    def __unicode__(self):
        return self.name + ' ( Code:' + self.code +' )'

