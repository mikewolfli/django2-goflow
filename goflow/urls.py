from django.urls import path,re_path, include #django 2.*

from django.conf import settings
from django.contrib.auth import logout, login

from goflow.apptools.forms import DefaultAppStartForm
from goflow.apptools.views import start_application, default_app
from goflow.runtime.views import *
from goflow.workflow.views import process_dot, index, cron

urlpatterns = [
    re_path(r'^.*/logout/$', logout, name='logout'),
    re_path(r'^.*/accounts/login/$', login,
        {'template_name': 'goflow/login.html'}),
    path('apptools/', include('goflow.apptools.urls')),
    path('graph/', include('goflow.graphics.urls')),
]

urlpatterns += [
    path('', index),
    path('process/dot/<int:id>/',process_dot),
    path('cron/', cron),
    ]

urlpatterns += [
    path('default_app/<int:id>/', default_app),
    re_path(r'^start/(?P<app_label>.*)/(?P<model_name>.*)/$', start_application),
    re_path(r'^start_proto/(?P<process_name>.*)/$', start_application,
        {'form_class':DefaultAppStartForm,
         'redirect':'../../',
         'template':'goflow/start_proto.html'}),
]

urlpatterns += [
    path('otherswork/',                 otherswork),
    path('otherswork/instancehistory/', instancehistory),
    path('myrequests/',                 myrequests),
    path('myrequests/instancehistory/', instancehistory),
    path('mywork/',                     mywork),
    path('mywork/activate/<int:id>/', activate),
    path('mywork/complete/<int:id>/', complete),
]

