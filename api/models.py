from django.db import models


class Product(models.Model):
    # Código de producto o ID (texto de longitud variable)
    code = models.CharField(max_length=200)

    # Precio de compra (número real)
    cost = models.DecimalField(decimal_places=2, max_digits=10)

    # Precio de venta al público (número real)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    # Descripción (texto de longitud variable)
    description = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=["code"]),
        ]