from django.urls import path, re_path

from goflow.apptools import forms
from goflow.apptools.views import *

urlpatterns = [
    re_path(r'^start/(?P<app_label>.*)/(?P<model_name>.*)/$', start_application),
    re_path(r'^start_proto/(?P<process_name>.*)/$', start_application, {'form_class':forms.DefaultAppStartForm, 'template':'goflow/start_proto.html'}),
    re_path(r'^view_application/(?P<id>\d+)/$', view_application),
    re_path(r'^choice_application/(?P<id>\d+)/$', choice_application),
    path('sendmail/', sendmail),
]
