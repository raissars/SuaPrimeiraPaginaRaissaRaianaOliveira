from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('autor/', views.criar_autor, name='criar_autor'),
    path('categoria/', views.criar_categoria, name='criar_categoria'),
    path('post/', views.criar_post, name='criar_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]
