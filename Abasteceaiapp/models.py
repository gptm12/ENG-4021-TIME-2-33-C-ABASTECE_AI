# Create your models here.

from django.db import models

class Posto(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    preco_gasolina = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    preco_etanol = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    preco_diesel = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class TipoCombustivel(models.Model):
    """Combustivel disponivel no posto."""
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Preco(models.Model):
    """Preco de um combustivel em um posto."""
    TIPOS = [
        ('gasolina', 'Gasolina Comum'),
        ('aditivada', 'Gasolina Aditivada'),
        ('etanol', 'Etanol'),
        ('diesel', 'Diesel S-10'),
    ]
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, related_name='precos')
    # tipo = models.CharField(max_length=20, choices=TIPOS)
    tipo_combustivel = models.ForeignKey(TipoCombustivel, on_delete=models.CASCADE, related_name='precos')
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.posto.nome} - {self.tipo}: R$ {self.valor}"


class Comodidade(models.Model):
    """Comercios disponiveis no posto (conveniencia, farmacia, etc)."""
    TIPOS = [
        ('conveniencia', 'Conveniencia'),
        ('farmacia', 'Farmacia'),
        ('restaurante', 'Restaurante'),
        ('loja', 'Loja'),
    ]
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, related_name='comodidades')
    tipo = models.CharField(max_length=20, choices=TIPOS)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
