from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.Board import views as board_views
from apps.Projects import views as project_views
from apps.Board import views
from django.urls import path
# import debug_toolbar # incomplete intergration


urlpatterns = [
    # Board's Url Patterns
    path('admin/', admin.site.urls),
    path('Board/', views.Board, name='board'),
    path('Board/create_board/', views.create_board, name='create_board'),
    path('Board/<int:board_id>/', views.board_detail, name='board_detail'),
    path('Board/<int:board_id>/create_list/', views.create_list, name='create_list'),
    path('Board/<int:list_id>/create_card/', views.create_card, name='create_card'),
    path('Board/', board_views.Board, name='board'),
    path('Board/create_board/', board_views.create_board, name='create_board'),
    path('Board/<int:board_id>/', board_views.board_detail, name='board_detail'),
    path('Board/<int:board_id>/create_list/', board_views.create_list, name='create_list'),
    path('Board/<int:list_id>/create_card/', board_views.create_card, name='create_card'),
    path('assign_issue/<int:issue_id>/', views.assign_issue, name='assign_issue'),
    
    #  Projects' Url Patterns
    path('Project', project_views.project_list, name='project_list'),
    path('New_Project/', project_views.create_project, name='create_project'),
    path('<int:project_id>/', project_views.project_detail, name='project_detail'),
    path('<int:project_id>/update_project/', project_views.update_project, name='update_project'),
    path('<int:project_id>/delete_project/', project_views.delete_project, name='delete_project'),
    path('<int:project_id>/create_issue/', project_views.create_issue, name='create_issue'),
    path('<int:issue_id>/', project_views.issue_detail, name='issue_detail'),
    path('<int:issue_id>/update_issue/', project_views.update_issue, name='update_issue'),
    path('<int:issue_id>/delete_issue/', project_views.delete_issue, name='delete_issue'),
# Users app url patterns
    path('assign_issue/<int:issue_id>/', views.assign_issue, name='assign_issue'),
    path('resolve_issue/<int:issue_id>/', views.resolve_issue, name='resolve_issue'),
    path('reassign_issue/<int:issue_id>/', views.reassign_issue, name='reassign_issue'),
    path('manage_roles/', views.manage_roles, name='manage_roles'),
    # path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
