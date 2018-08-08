from django.urls import path
from goflow.graphics2 import views as goflow_graphics2_views


urlpatterns = [
    path('processimage/<int:process_id>/pos_activity/', goflow_graphics2_views.pos_activity),
]
