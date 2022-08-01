
from django.urls import path 
from . import views

urlpatterns = [
    path('',views.valute, name='valute'),
]