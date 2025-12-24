from django.urls import path
from .views import *
urlpatterns = [
    path('projects/',projects, name = 'projects'),
    path('projects/<uuid:id>',project, name = 'project'),
]