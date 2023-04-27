from django.urls import path
from . import views


from django.urls import path
from . import views
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    # React Render
    path('api/boards/', views.board_list, name='board_list'),
    path('api/boards/<int:board_id>/', views.board_detail, name='board_detail'),
    path('api/boards/create/', views.create_board, name='create_board'),
    path('api/boards/<int:board_id>/update/', views.update_board, name='update_board'),
    path('api/boards/<int:board_id>/delete/', views.delete_board, name='delete_board'),
    path('api/boards/<int:board_id>/create_list/', views.create_list, name='create_list'),
    path('api/lists/<int:list_id>/create_card/', views.create_card, name='create_card'),
    path('api/issues/<int:issue_id>/assign/', views.assign_issue, name='assign_issue'),
    path('api/issues/<int:issue_id>/resolve/', views.resolve_issue, name='resolve_issue'),
    path('api/issues/<int:issue_id>/reassign/', views.reassign_issue, name='reassign_issue'),
    path('api/roles/<int:role_id>/manage/', views.manage_roles, name='manage_roles'),
    # URL patterns for React app
    path('', views.react_app, name='react_app'),
    # Html Render
    path('', views.board_list, name='board_list'),
    path('<int:board_id>/', views.board_detail, name='board_detail'),
    path('create/', views.create_board, name='create_board'),
    path('<int:board_id>/update/', views.update_board, name='update_board'),
    path('<int:board_id>/delete/', views.delete_board, name='delete_board'),
    path('<int:board_id>/create_list/', views.create_list, name='create_list'),
    path('<int:list_id>/create_card/', views.create_card, name='create_card'),
    # other URL patterns...
]