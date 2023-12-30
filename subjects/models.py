from django.db import models

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    year = models.CharField(max_length=4, blank=True)
    exam = models.BooleanField(blank=True)
    
    def __str__(self):
        return self.subject