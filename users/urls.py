from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_users_list, name='list'),
    path('pairs/', views.get_pairs, name='pairs'),
]
