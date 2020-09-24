from django.contrib import admin
from .models import Event, Discipline, Distance, Format, Organiser, EventInstance

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'organiser',
        'discipline',
        'distance',
        'exact_distance_km',
        'event_format',
        'sku',
        'event_instance',
        'entrycutoff',
        'keyinfo',
        'description',
        'location_post_code',
        'latitude',
        'longitude',
        'price',
        'rating',
        'image_url',
        'image',
    )

    ordering = ('name',)

class DisciplineAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class DistanceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class FormatAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class OrganiserAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class EventInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'event_date',
        'race_limit',
    )


admin.site.register(Event, EventAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Distance, DistanceAdmin)
admin.site.register(Format, FormatAdmin)
admin.site.register(Organiser, OrganiserAdmin)
admin.site.register(EventInstance, EventInstanceAdmin)