from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('<int:board_id>/', views.board_detail, name='board_detail'),
    path('create/', views.create_board, name='create_board'),
    path('<int:board_id>/update/', views.update_board, name='update_board'),
    path('<int:board_id>/delete/', views.delete_board, name='delete_board'),
    path('<int:board_id>/create_list/', views.create_list, name='create_list'),
    path('<int:list_id>/create_card/', views.create_card, name='create_card'),
    # other URL patterns...
]