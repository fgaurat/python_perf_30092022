from django.urls import path

from . import views

urlpatterns = [
    path('toto', views.index, name='index'),
]