from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Signup(models.Model):
    email=models.EmailField()
    full_name=models.CharField(max_length=120 , blank=True ,null=True)
    timestamp=models.DateTimeField(auto_now_add=True , auto_now=False,null=True )
    updated=models.DateTimeField(auto_now_add=False , auto_now=False,default=timezone.now)


    def __unicode__(self):
        return self.email