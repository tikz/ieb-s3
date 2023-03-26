import logging
import random
import threading
import time
from decimal import Decimal

from api.models import Product


class PriceUpdaterThread(threading.Thread):
    def run(self):
        while True:
            for product in Product.objects.all():
                multiplier = Decimal(1 + random.randint(-50, 50)/500)
                product.cost = product.cost * multiplier
                product.price = product.price * multiplier
                product.save()

                multiplier_format = f"{(1-multiplier)*100:+.2f}"
                new_prices = f"cost={product.cost:.2f} price={product.price:.2f}"
                logging.info(f"Actualizado {product.code: <10} {multiplier_format}% \t {new_prices}")

            time.sleep(random.randint(1, 10))
