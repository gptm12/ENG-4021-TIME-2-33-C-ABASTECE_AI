from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Comodidade, Posto,Preco


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
    return render(request, 'detalhes.html', {'posto': posto})


def perfil_view(request):
    return render(request, 'perfil.html')

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
        posto = Posto.objects.update(
            nome=request.POST.get('nome'),
            endereco=request.POST.get('endereco'),
            latitude=request.POST.get('latitude'),
            longitude=request.POST.get('longitude'),
        )
        return render(request, 'detalhes.html', {'posto': posto})
    else:
        return render(request, 'forms_posto.html', context={'action': 'Atualizar'})
    
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
    if request.method == 'POST':
        tipo_combustivel = request.POST.get('tipo_combustivel')
        preco = request.POST.get('valor')

        preco = Preco.objects.update(
            tipo_combustivel=tipo_combustivel,
            valor=preco,
            posto=get_object_or_404(Posto, id=request.POST.get('posto')),
        )
        return render(request, 'detalhes.html', {'preco': preco})
    else:
        return render(request, 'forms_preco.html', context={'action': 'Atualizar', 'postos': Posto.objects.all()})   

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
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nome = request.POST.get('nome')
    
        comodidade = Comodidade.objects.update(
            posto=get_object_or_404(Posto, id=request.POST.get('posto')),
            tipo=tipo,
            nome=nome,
        )
        return render(request, 'detalhes.html', {'comodidade': comodidade})
    else:
        postos = Posto.objects.all()
        return render(request, 'forms_comodidade.html', context={'action': 'Atualizar', 'postos': postos})
    
        

