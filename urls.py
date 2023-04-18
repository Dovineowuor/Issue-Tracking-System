from django.urls import path, include
from . import views
from Projects.views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', include('apps.Projects.urls')), # updated the include path
    # other URL patterns...
]

