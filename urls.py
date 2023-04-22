from django.urls import path, include
from . import views
from apps.Projects.views import *

from django.urls import path
from . import views

urlpatterns = [
    path('<path:path>/', views.some_view)
    re_path(r'^(?P<path>.*)$', views.some_view)
    path('', views.project_list, name='project_list'),
    path('create_project/', views.create_project, name='create_project'),
    path('<int:project_id>/', views.project_detail, name='project_detail'),
    path('<int:project_id>/update_project/', views.update_project, name='update_project'),
    path('<int:project_id>/delete_project/', views.delete_project, name='delete_project'),
    path('<int:project_id>/create_issue/', views.create_issue, name='create_issue'),
    path('<int:issue_id>/', views.issue_detail, name='issue_detail'),
    path('<int:issue_id>/update_issue/', views.update_issue, name='update_issue'),
    path('<int:issue_id>/delete_issue/', views.delete_issue, name='delete_issue'),

]