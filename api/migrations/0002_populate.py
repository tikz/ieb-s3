from decimal import Decimal

from django.db import migrations, transaction

# Poblar tabla con 2 productos de ejemplo

def populate(apps, schema_editor):
    Product = apps.get_model('api', 'Product')

    with transaction.atomic():
        Product.objects.create(code="R129", cost=Decimal(2200), price=Decimal(6000), description="Remera de algodón puro hipoalergénico.")
        Product.objects.create(code="F600-L-X", cost=Decimal(5000), price=Decimal(19000), description="Llanta original de Fiat 600, en buen estado.")


def clear(apps, schema_editor):
    Product = apps.get_model('api', 'Product')

    with transaction.atomic():
        Product.objects.filter(code="R129").delete()
        Product.objects.filter(code="F600-L-X").delete()

class Migration(migrations.Migration):
    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate, clear),
    ]
