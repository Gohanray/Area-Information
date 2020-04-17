from django.urls import path
from . import views

print(path)
urlpatterns=[
    path('', views.home, name='home'),
    path('calculate/', views.calculate, name='calculate')
]