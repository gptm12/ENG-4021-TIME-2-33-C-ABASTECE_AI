from django.db import models

# Create your models here.

"""class Posto(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    precos =models.DateField()

    def __str__(self):
        return self.nome"""
"""Modelagem de dados do AbasteceAi.

Cada classe vira uma tabela no banco quando eu rodar as migracoes.
"""

class Posto(models.Model):
    """Representa um posto de combustivel."""
    nome = models.CharField(max_length=100)
    bandeira = models.CharField(max_length=50, blank=True)
    endereco = models.CharField(max_length=200)
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Texto que aparece no admin
        return self.nome


class Preco(models.Model):
    """Preco de um combustivel em um posto."""
    TIPOS = [
        ('gasolina', 'Gasolina Comum'),
        ('aditivada', 'Gasolina Aditivada'),
        ('etanol', 'Etanol'),
        ('diesel', 'Diesel S-10'),
    ]
    posto = models.ForeignKey(Posto, on_delete=models.CASCADE, related_name='precos')
    tipo = models.CharField(max_length=20, choices=TIPOS)
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
