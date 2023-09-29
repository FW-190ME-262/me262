from django.contrib.admindocs import views
from django.urls import path, include

urlpatterns = [
    path('home', views.home, name='home'),
    path('modeli/', views.modeli, name='modeli'),
    path('contakt/', views.contakt, name='contakt'),

]
