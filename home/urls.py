from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.index, name="index"),
    path('sobre/', views.sobre, name="sobre"),
    path('contato/', views.contato, name="contato"),
    path('item/<int:id>/', views.exibir_item, name="exibir_item"),

    # Lista de produtos
    path('produtos/', views.produtos, name="lista_produtos"),
    path('produto/', views.produtos, name="produto"),  # Mantido para /produto/ funcionar, aponta para a mesma view

    # Formulário de produto
    path('produto/form/', views.form_produto, name="form_produto"),

    # Dia da semana
    path('diasemana/<int:num>/', views.diasemana, name="diasemana"),
]
