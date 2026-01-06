from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='root'),
    path('home/', views.home, name='home'),
    path('collections/', views.collections, name='collections'),
    path('story/', views.story, name='story'),
]