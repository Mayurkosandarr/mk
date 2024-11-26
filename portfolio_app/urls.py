from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutme/', views.aboutme_update, name='aboutme_update'),
    path('education/', views.education_list, name='education_list'),
    path('project/', views.project_list, name='project_list'),
    path('education/', views.education_list, name='education_list'), 
    path('project/create/', views.ProjectCreateView.as_view(), name='project_create'), 
    path('project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
]
