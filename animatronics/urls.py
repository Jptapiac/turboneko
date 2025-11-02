from django.urls import path
from . import views


app_name = 'animatronics'

urlpatterns = [
    path('', views.animatronic_list, name='list'),
]


