from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_users_list, name='list'),
    path('rounds/', views.get_rounds, name='rounds'),
    path('pairs/', views.get_pairs, name='pairs'),
    path('round/make/', views.make_round, name='round_make')
]