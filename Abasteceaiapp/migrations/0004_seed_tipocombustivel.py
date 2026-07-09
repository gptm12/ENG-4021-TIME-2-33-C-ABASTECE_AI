from django.db import migrations


TIPOS = [
    ("Gasolina Comum", "Gasolina comum, sem aditivos."),
    ("Gasolina Aditivada", "Gasolina com aditivos de limpeza para o motor."),
    ("Etanol", "Etanol hidratado combustível."),
    ("Diesel S10", "Óleo diesel com baixo teor de enxofre (S10)."),
    ("Diesel S500", "Óleo diesel comum (S500)."),
    ("GNV", "Gás Natural Veicular."),
]


def seed_tipos(apps, schema_editor):
    TipoCombustivel = apps.get_model('Abasteceaiapp', 'TipoCombustivel')
    for titulo, descricao in TIPOS:
        TipoCombustivel.objects.get_or_create(titulo=titulo, defaults={'descricao': descricao})


def remove_tipos(apps, schema_editor):
    TipoCombustivel = apps.get_model('Abasteceaiapp', 'TipoCombustivel')
    TipoCombustivel.objects.filter(titulo__in=[t[0] for t in TIPOS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('Abasteceaiapp', '0003_conta'),
    ]

    operations = [
        migrations.RunPython(seed_tipos, remove_tipos),
    ]
