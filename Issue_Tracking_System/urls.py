from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.Board import views
from .views import board_list
from django.urls import path
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Board/', views.board, name='board'),
    path('Board/', board_list, name='board_list'),
    path('Board/create_board/', views.create_board, name='create_board'),
    path('Board/<int:board_id>/', views.board_detail, name='board_detail'),
    path('Board/<int:board_id>/create_list/', views.create_list, name='create_list'),
    path('Board/<int:list_id>/create_card/', views.create_card, name='create_card'),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
