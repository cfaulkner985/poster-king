from django.contrib import admin
from .models import Person, Product

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'dob',
        'place',
    )

    ordering = ('sku',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Person, PersonAdmin)
admin.site.register(Product, ProductAdmin)
