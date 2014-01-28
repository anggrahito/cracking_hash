'''
Created on Jan 28, 2014

@author: itox
'''
from django.db import models
from django import forms

class Hashtext(models.Model):
    input_hash = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.input_hash

class Hashlength(models.Model):
    input_length = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.input_length
    
class Inputtext(models.Model):
    input_text = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return self.input_text
    
class CrackResult(models.Model):
    input_hash = models.ForeignKey(Hashtext)
    input_length = models.ForeignKey(Hashlength)
    status = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.input_hash
    
class CalcResult(models.Model):
    input_text = models.ForeignKey(Inputtext)
    status = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.input_text
    
class UploadFileHashes(forms.Form):
    input_file = forms.FileField()
    

class HashPasswordlist(models.Model):
    input_filex = models.FileField(upload_to='Documents', blank=True, null=True)
    hasil = models.CharField(max_length=255, blank=True)    

    def __unicode__(self):
       return self.hasil