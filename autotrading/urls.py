
from django.urls import path

import autotrading.auto_connect

from . import views

urlpatterns = [
    path('', views.main_index, name='main'),
    path('insertkey/', views.inserkey, name='insertkey'),
    path('deletekey/', autotrading.auto_connect.stop_autotrade, name='deletekey')
]