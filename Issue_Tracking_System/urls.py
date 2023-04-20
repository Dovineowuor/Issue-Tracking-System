from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.Board import views as board_views
from apps.Projects import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', board_views.board, name='board'),
    path('board/create_board/', board_views.create_board, name='create_board'),
    path('board/<int:board_id>/', board_views.board_detail, name='board_detail'),
    path('board/<int:board_id>/create_list/', board_views.create_list, name='create_list'),
    path('board/<int:list_id>/create_card/', board_views.create_card, name='create_card'),
    path('', project_views.project_list, name='project_list'),
    path('create_project/', project_views.create_project, name='create_project'),
    path('<int:project_id>/', project_views.project_detail, name='project_detail'),
    path('<int:project_id>/update_project/', project_views.update_project, name='update_project'),
    path('<int:project_id>/delete_project/', project_views.delete_project, name='delete_project'),
    path('<int:project_id>/create_issue/', project_views.create_issue, name='create_issue'),
    path('<int:issue_id>/', project_views.issue_detail, name='issue_detail'),
    path('<int:issue_id>/update_issue/', project_views.update_issue, name='update_issue'),
    path('<int:issue_id>/delete_issue/', project_views.delete_issue, name='delete_issue')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)