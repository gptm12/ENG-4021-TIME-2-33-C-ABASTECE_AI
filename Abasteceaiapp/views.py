# Create your views here.
from django.shortcuts import render
from sprint5.models import Posto
from django.http import HttpResponse

# Create your views here.# sprint5/views.py

def home(request):
    """View para a página inicial"""
    return render(request, 'home.html')  # ou use HttpResponse para teste
    # return HttpResponse("<h1>Bem-vindo ao Sistema de Postos</h1>")
"""def home(request):
    postos = Posto.objects.all()
    return render(request, 'home.html', {'postos': postos})
    return render(request, 'detalhes_do_posto.html')"""
def login_view(request):
    # Pagina inicial: tela de login
    return render(request, 'login.html')


def home_view(request):
    # Busca todos os postos do banco para listar na home
    postos = Posto.objects.all()
    return render(request, 'home.html', {'postos': postos})


def detalhes_view(request, posto_id):
    # Pega o posto pelo id ou mostra erro 404
    posto = get_object_or_404(Posto, id=posto_id)
    return render(request, 'detalhes.html', {'posto': posto})


def perfil_view(request):
    # Por enquanto so renderiza a tela com dados fixos no HTML
    return render(request, 'perfil.html')