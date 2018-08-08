from django.urls import path, re_path

from goflow.apptools.views import image_update, app_env, test_start

urlpatterns = [
    path('icon/image_update/', image_update),
    re_path(r'^application/testenv/(?P<action>create|remove)/(?P<id>.*)/$', app_env),
    path('application/teststart/<int:id>/', test_start),
]
