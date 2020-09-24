from django.contrib import admin
from .models import Event, Discipline, Distance, Format, Organiser, EventInstance

# Register your models here.

admin.site.register(Event)
admin.site.register(Discipline)
admin.site.register(Distance)
admin.site.register(Format)
admin.site.register(Organiser)
admin.site.register(EventInstance)

