from django.contrib import admin
from .models import Event

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


admin.site.register(Event, EventAdmin)
