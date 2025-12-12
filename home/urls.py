from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('item/<int:id>', views.exibir_item, name="exibir_item"),
    path('produto/', views.produto, name="produto"),

    
    # 👉 ADICIONE ESTA LINHA
    path('diasemana/<int:num>/', views.diasemana, name="diasemana"),
]

