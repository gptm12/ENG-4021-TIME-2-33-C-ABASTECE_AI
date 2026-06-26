"""
URL configuration for Abasteceai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from Abasteceaiapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/home/')),
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('api/postos.geojson', views.postos_geojson, name='postos-geojson'),
    path('posto/<int:posto_id>/', views.detalhes_view, name='detalhes'),
    path('perfil/', views.perfil_view, name='perfil'),
    path('adicionar_posto/', views.adicionar_posto_view, name='adicionar-posto'),
    path('atualizar_posto/<int:posto_id>/', views.atualizar_posto_view, name='atualizar-posto'),
    path('adicionar_preco/', views.adicionar_preco_view, name='adicionar-preco'),
    path('atualizar_preco/<int:preco_id>/', views.atualizar_preco_view, name='atualizar-preco'),
    path('adicionar_comodidade/', views.adicionar_comodidade_view, name='adicionar-comodidade'),
    path('atualizar_comodidade/<int:comodidade_id>/', views.atualizar_comodidade_view, name='atualizar-comodidade'),
]