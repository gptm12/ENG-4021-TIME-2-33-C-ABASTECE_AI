from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Posto


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