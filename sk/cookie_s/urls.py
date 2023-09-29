from . import views
from django.urls import path


urlpatterns = [path('home', views.homepage, name='home'),
               path('cookie/', views.dalete_cookie, name='delite')]
