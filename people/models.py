from django.db import models


class Person(models.Model):
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    dob = models.DateField()
    place = models.CharField(max_length=254)


    def __str__(self):
        return self.name
