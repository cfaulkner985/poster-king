from django.db import models


class Event(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    date = models.DateField()
    city = models.CharField(max_length=254)
    venue = models.CharField(max_length=254)

    def __str__(self):
        return self.name
