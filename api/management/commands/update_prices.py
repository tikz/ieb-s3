import random
import time
from decimal import Decimal

from django.core.management.base import BaseCommand, CommandError

from api.models import Product


class Command(BaseCommand):
    help = 'Actualiza los precios de todos los productos (al azar)'

    def handle(self, *args, **options):
        while True:
            for product in Product.objects.all():
                multiplier = Decimal(1 + random.randint(-5, 5)/100)
                product.cost = product.cost * multiplier
                product.price = product.price * multiplier
                product.save()

                multiplier_format = f"{(1-multiplier)*100:+.2f}"
                new_prices = f"cost={product.cost:.2f} price={product.price:.2f}"
                self.stderr.write(self.style.SUCCESS(f"Actualizado {product.code: <10} {multiplier_format}% \t {new_prices}"))
            time.sleep(random.randint(1,5))