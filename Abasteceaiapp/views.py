from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from .models import Comodidade, Conta, Posto,Preco


def home(request):
    postos = Posto.objects.all()
    return render(request, 'home.html', {'postos': postos})


def login_view(request):
    return render(request, 'login.html')


def postos_geojson(request):
    postos = Posto.objects.all()
    features = []
    for posto in postos:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(posto.longitude), float(posto.latitude)]
            },
            "properties": {
                "nome": posto.nome,
                "endereco": posto.endereco,
                "gasolina": str(posto.preco_gasolina) if posto.preco_gasolina else "–",
                "etanol": str(posto.preco_etanol) if posto.preco_etanol else "–",
                "diesel": str(posto.preco_diesel) if posto.preco_diesel else "–",
            }
        })
    return JsonResponse({"type": "FeatureCollection", "features": features})


def detalhes_view(request, posto_id):
    posto = get_object_or_404(Posto, id=posto_id)
    precos = posto.precos.all()
    comodidades = posto.comodidades.all()
    return render(request, 'detalhes.html', {'posto': posto, 'precos': precos, 'comodidades': comodidades})


def perfil_view(request):
    conta = get_object_or_404(Conta, id=request.GET.get('conta_id'))
    return render(request, 'perfil.html', {'conta': conta})

def adicionar_posto_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        posto = Posto.objects.create(
            nome=nome,
            endereco=endereco,
            latitude=latitude,
            longitude=longitude,
        )
        return render(request, 'detalhes.html', {'posto': posto})
    else:
        return render(request, 'forms_posto.html',context={'action': 'Adicionar'})
    
def atualizar_posto_view(request,posto_id):
    posto = get_object_or_404(Posto, id=posto_id)
    if request.method == 'POST':
        posto.nome = request.POST.get('nome')
        posto.endereco = request.POST.get('endereco')
        posto.latitude = request.POST.get('latitude')
        posto.longitude = request.POST.get('longitude')
        posto.save()
        return render(request, 'detalhes.html', {'posto': posto})
    else:
        return render(request, 'atualiza_forms_posto.html', context={'action': 'Atualizar', 'posto': posto})
    
def deletar_posto_view(request, posto_id):
    posto = get_object_or_404(Posto, id=posto_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            posto.delete()
            return render(request, 'home.html', {'message': 'Posto deletado com sucesso.'})
    return render(request, 'temcerteza.html', {'posto': posto})
  
    
def adicionar_preco_view(request):
    if request.method == 'POST':
        tipo_combustivel = request.POST.get('tipo_combustivel')
        preco = request.POST.get('valor')

        preco = Preco.objects.create(
            tipo_combustivel=tipo_combustivel,
            valor=preco,
            posto=get_object_or_404(Posto, id=request.POST.get('posto')),
        )
        return render(request, 'detalhes.html', {'preco': preco})
    else:
        return render(request, 'forms_preco.html', context={'action': 'Adicionar', 'postos': Posto.objects.all()})

def atualizar_preco_view(request):
    preco = get_object_or_404(Preco, id=request.POST.get('preco_id'))
    if request.method == 'POST':
        tipo_combustivel = request.POST.get('tipo_combustivel')
        valor = request.POST.get('valor')
        preco.tipo_combustivel = tipo_combustivel
        preco.valor = valor
        preco.save()
        return render(request, 'detalhes.html', {'preco': preco})
    else:
        return render(request, 'forms_preco.html', context={'action': 'Atualizar', 'postos': Posto.objects.all()})   
    
def deletar_preco_view(request, preco_id):
    preco = get_object_or_404(Preco, id=preco_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            preco.delete()
            return render(request, 'detalhes.html', {'message': 'Preço deletado com sucesso.'})
    return render(request, 'temcerteza.html', {'preco': preco})

def adicionar_comodidade_view(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nome = request.POST.get('nome')
        comodidade = Comodidade.objects.create(
            posto=get_object_or_404(Posto, id=request.POST.get('posto')),
            tipo=tipo,
            nome=nome,
        )
        return render(request, 'detalhes.html', {'comodidade': comodidade})
    else:
        postos = Posto.objects.all()
        return render(request, 'forms_comodidade.html', context={'action': 'Adicionar','postos': postos})
    
def atualizar_comodidade_view(request):
    comodidade = get_object_or_404(Comodidade, id=request.POST.get('comodidade_id'))
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nome = request.POST.get('nome')
        comodidade.tipo = tipo
        comodidade.nome = nome
        comodidade.save()
        return render(request, 'detalhes.html', {'comodidade': comodidade})
    else:
        postos = Posto.objects.all()
        return render(request, 'forms_comodidade.html', context={'action': 'Atualizar', 'postos': postos})
    
def deletar_comodidade_view(request, comodidade_id):
    comodidade = get_object_or_404(Comodidade, id=comodidade_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            comodidade.delete()
            return render(request, 'detalhes.html', {'message': 'Comodidade deletada com sucesso.'})
    return render(request, 'temcerteza.html', {'comodidade': comodidade})
    
def criar_conta_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        conta = Conta.objects.create(
            usuario=usuario,
            email=email,
            senha=senha,
        )
        return render(request, 'perfil.html', {'conta': conta})
    else:
        return render(request, 'forms_conta.html', context={'action': 'Adicionar'})

def atualizar_conta_view(request):
    conta = get_object_or_404(Conta, id=request.POST.get('conta_id'))
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        conta.usuario = usuario
        conta.email = email
        conta.senha = senha
        conta.save()
        return render(request, 'perfil.html', {'conta': conta})
    else:
        return render(request, 'forms_conta.html', context={'action': 'Atualizar'})
    
def deletar_conta_view(request, conta_id):
    conta = get_object_or_404(Conta, id=conta_id)
    if request.method == 'POST':
        if 'confirm' in request.POST:
            conta.delete()
            return render(request, 'home.html', {'message': 'Conta deletada com sucesso.'})
    return render(request, 'temcerteza.html', {'conta': conta})