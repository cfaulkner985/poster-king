from django.contrib import admin
from .models import Person

# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'dob',
        'place',
    )

    ordering = ('sku',)


admin.site.register(Person, PersonAdmin)

