from django.db import models


class Product(models.Model):

    class Meta:
        verbose_name_plural = 'Product'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Event(models.Model):
    product = models.ForeignKey('Product', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    date = models.DateField()
    city = models.CharField(max_length=254)
    venue = models.CharField(max_length=254)

    def __str__(self):
        return self.name