from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.get_users_list, name='list'),
    path('pairs/', views.get_pairs, name='pairs'),
    path('pairs/add/', views.add, name='add'),
    path('pairs/save/', views.save, name='save'),
]
