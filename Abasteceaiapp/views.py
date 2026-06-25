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
        return render(request, 'forms_posto.html')
    
def adicionar_preco_view(request):
    if request.method == 'POST':
        tipo_combustivel = request.POST.get('tipo_combustivel')
        preco = request.POST.get('valor')

        preco = Preco.objects.create(
            tipo_combustivel=tipo_combustivel,
            valor=preco
        )
        return render(request, 'detalhes.html', {'preco': preco})

def adicionar_comodidade_view(request):
    if request.method == 'POST':
       conveniencia = request.POST.get('conveniencia')
       farmacia = request.POST.get('farmacia')
       restaurante = request.POST.get('restaurante')
       loja = request.POST.get('loja')
    
    comodidade = Comodidade.objects.create(
        posto=posto,
        tipo=tipo,
        nome=nome,
    )
    return render(request, 'detalhes.html', {'comodidade': comodidade})

        

