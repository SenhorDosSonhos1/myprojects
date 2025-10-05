from django.urls import path
from . import views

urlpatterns = [
    path('adicionar/', views.adicionar, name='adicionar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('editar/<int:id>/', views.editar, name='editar')
]
