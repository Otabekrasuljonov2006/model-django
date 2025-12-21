from django.urls import path
from .views import *
urlpatterns = [
    path('news/',news),
    path('new/<int:id>',yangilik),
    path('shartli/<int:son>',shartli),
]