from django.contrib import admin
from .models import Event, Product

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'date',
        'city',
        'venue',
    )

    ordering = ('sku',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Product, ProductAdmin)
