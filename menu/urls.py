from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('menus/', views.menus, name='menus'),
    path('menus/details/<int:id>', views.details, name='details'),
]