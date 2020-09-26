from django.contrib import admin

from .models import Club

# Register your models here.

class ClubAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Club, ClubAdmin)