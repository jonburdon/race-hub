from django.contrib import admin

from .models import Club

# Register your models here.

class ClubAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = (
        'id',
        'friendly_name',
        'name',
    )

admin.site.register(Club, ClubAdmin)