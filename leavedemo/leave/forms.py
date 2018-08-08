#!/usr/local/bin/python
# -*- coding: utf-8 -*-


from goflow.apptools.forms import BaseForm, StartForm

# allows calendar widgets
from django import forms

from leavedemo.leave.models import LeaveRequest, LeaveAttachment
from django.forms import ModelForm, inlineformset_factory, ValidationError
from django.contrib.admin import widgets


class StartRequestForm(StartForm):
    day_start = forms.DateField(widget=widgets.AdminDateWidget)
    day_end = forms.DateField(widget=widgets.AdminDateWidget)
    
    def save(self, user, data=None, commit=True):
        ''' overriden for adding the requester
        '''
        obj = super(StartForm, self).save(commit=False)
        obj.requester = user
        obj.save()
        return obj
    
    class Meta:
         model = LeaveRequest
         exclude = ('reason_denial', 'requester')

class RequesterForm(BaseForm):
    class Meta:
         model = LeaveRequest
         exclude = ('reason_denial', 'requester')

class CheckRequestForm(BaseForm):
    class Meta:
         model = LeaveRequest
         fields = ('reason_denial',)

class LeaveAttachmentForm(ModelForm):
    
    class Meta:
        model = LeaveAttachment
        exclude = []
 
        
LeaveAttachmentFormSet = inlineformset_factory(
    LeaveRequest, LeaveAttachment, fields=('attachment','description'), extra=4)
