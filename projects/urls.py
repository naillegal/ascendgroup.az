from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:pk>/<str:slug>/', views.project_detail, name='project-detail'),
]