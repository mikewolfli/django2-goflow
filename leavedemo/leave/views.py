#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from goflow.apptools import views as goflow_apptools_views
from .models import  Account

def checkstatus_auto(request, workitem=None, notif_user=False):
    # print workitem
    workitem.instance.condition = 'OK: Forward to supervisor'
    return True


def start_leave_request(request, process_name, form_class, formset, template):
    user = request.user

    objs = Account.objects.filter(user=user)

    return goflow_apptools_views.start_application(request= request, process_name=process_name, form_class=form_class, formset=formset, template=template, extra_context={'objs':objs})
