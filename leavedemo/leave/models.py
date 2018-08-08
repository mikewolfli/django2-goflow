#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Group, User
from django.utils.safestring import mark_safe
# Create your models here.

LEAVE_ROOT = 'leave'

class LeaveRequest(models.Model):
    TYPE_CHOICES = (
            ('Vacation','Vacation'),
            ('Birth or marriage of child','Birth or marriage of child'),
            ('Change of residence','Change of residence'),
            ('Death of a child','Death of a child'),
            ('Death of a relative in the ascending line','Death of a relative in the ascending line'),
            ('Death of parent-in-law, brother or sister','Death of parent-in-law, brother or sister'),
            ('Death of spouse','Death of spouse'),
            ('Marriage','Marriage'),
            ('Maternity','Maternity'),
            ('Serious illness of a child','Serious illness of a child'),
            ('Serious illness of a relative in the asc line','Serious illness of a relative in the asc line'),
            ('Serious illness of a parent-in-law','Serious illness of a parent-in-law'),
            ('Serious illness of spouse','Serious illness of spouse'))
    date = models.DateTimeField(auto_now=True)
    day_start = models.DateField()
    day_end = models.DateField()
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Vacation')
    reason = models.TextField(null=True, blank=True)
    reason_denial = models.TextField(null=True, blank=True, verbose_name='reason of denial')
    requester = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __unicode__(self):
        return 'leaverequest-%s' % str(self.pk)

class Manager(models.Model):
    MANAGER_CHOICES = (
                       ('secretary','Secretary'),
                       ('supervisor','Supervisor'),
                       )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='manager_set')
    category = models.CharField(max_length=50, choices=MANAGER_CHOICES, help_text='secretary, supervisor, ...')
    users = models.ManyToManyField(User, related_name='managers')
    def __unicode__(self):
        return '%s as %s' % (self.user.username, self.category)
    
class Account(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='accounts')
    category = models.CharField(max_length=50, help_text='vacations, rtt, ..')
    days = models.IntegerField(default=0)
    
    def __unicode__(self):
        return '%s-%s' % (self.user.username, self.category)

        
class LeaveAttachment(models.Model):
    leave = models.ForeignKey(
        LeaveRequest, on_delete=models.CASCADE, verbose_name="Leave Request")
    attachment = models.ImageField(upload_to=LEAVE_ROOT)
    description = models.CharField(
        "Description", max_length=255, blank=True, null=True)

    def image_tag(self):
        return mark_safe('<img src="%s" width="25" height="25" />' % self.attachment.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    class Meta:
        verbose_name = "Leave Attachment"
        verbose_name_plural = verbose_name
