from django.urls import path

from goflow.graphics import views

urlpatterns = [
    path('<int:id>/save/', views.graph_save),
    path('<int:id>/', views.graph, {'template':'goflow/graphics/graph.html'}),
]
