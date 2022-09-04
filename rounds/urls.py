from django.urls import path

from . import views

urlpatterns = [
    path('<int:round_id>/', views.get_round, name='round'),
    path('make/', views.make_round, name='round_make'),
    path('validate/', views.validate_round, name='validate'),
    path('validate/save', views.save, name='save')
]
