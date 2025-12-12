# views.py
from django.shortcuts import render, HttpResponse
from .forms import ContatoForm, ProdutoForm

# -----------------------------
# VIEWS DE HOME
# -----------------------------
def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

# -----------------------------
# VIEW DE CONTATO
# -----------------------------
def contato(request):
    form = ContatoForm()
    return render(request, 'contato.html', {'form': form})

# -----------------------------
# VIEW PARA EXIBIR ITEM POR ID
# -----------------------------
def exibir_item(request, id):
    return render(request, 'exibir_item.html', {'id': id})

# -----------------------------
# VIEW DO DIA DA SEMANA
# -----------------------------
def diasemana(request, num):
    dias = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
    if num < 0 or num > 6:
        return HttpResponse("Dia inválido")
    return HttpResponse(dias[num])

# -----------------------------
# VIEWS DE PRODUTOS
# -----------------------------
def produtos(request):
    lista = [
        {'id': 1, 'nome': 'Notebook', 'preco': '2.500,00'},
        {'id': 2, 'nome': 'Monitor', 'preco': '500,00'},
        {'id': 3, 'nome': 'Teclado', 'preco': '80,00'},
        {'id': 4, 'nome': 'Mouse', 'preco': '40,00'},
        {'id': 5, 'nome': 'Impressora', 'preco': '600,00'},
        {'id': 6, 'nome': 'Scanner', 'preco': '700,00'},
        {'id': 7, 'nome': 'Câmera Web', 'preco': '150,00'},
        {'id': 8, 'nome': 'Headset', 'preco': '120,00'},
        {'id': 9, 'nome': 'Pendrive 32GB', 'preco': '30,00'},
        {'id': 10, 'nome': 'HD Externo 1TB', 'preco': '350,00'},
        {'id': 11, 'nome': 'Estabilizador', 'preco': '200,00'},
        {'id': 12, 'nome': 'Switch 8 portas', 'preco': '180,00'},
        {'id': 13, 'nome': 'Roteador Wi-Fi', 'preco': '220,00'},
    ]
    return render(request, 'produto/lista.html', {'lista': lista})

# Formulário de produto
def form_produto(request):
    form = ProdutoForm()
    return render(request, 'produto/formulario.html', {'form': form})
