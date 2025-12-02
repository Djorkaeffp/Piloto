from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse ("""
        <h1>Bem-vindo ao Sistema</h1>

        <a href='/sobre/'><button>Ir para Sobre</button></a>
        <a href='/contato/'><button>Ir para Contato</button></a>
    """)

def sobre(request):
    return HttpResponse ("""
        <h1>Página Sobre</h1>
        <p>Informações sobre o sistema.</p>

        <a href='/'><button>Voltar para Home</button></a>
    """)

def contato(request):
    return HttpResponse("""
        <h1>Página de Contato</h1>
        <p>Fale conosco!
        Se desejar saber mais entre em contato vi e-mail: djorkaeffoliveira7@gmail.com</p>

        <a href='/'><button>Voltar para Home</button></a>
    """)