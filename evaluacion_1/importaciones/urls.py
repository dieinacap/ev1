from django.urls import path
from . import views

urlpatterns = [
    path('importacion/', views.importacion, name='importacion'),
    path('simulaciones/', views.lista_simulaciones, name='lista_simulaciones'),
]