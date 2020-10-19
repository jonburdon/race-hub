from import_export.admin import ImportExportModelAdmin
from django.contrib import admin

from .models import Result

# Register your models here.

from import_export import resources
from .models import Result

class ResultDownload(resources.ModelResource):

    class Meta:
        model = Result

class ResultsAdmin(ImportExportModelAdmin):
    list_display = (
        'eventinstance',
        'athletefirstname',
        'athletesurname',
        'athlete',
        'gender',
        'bibnumber',
        'agecat',
        'club',
        'chiptime',
        'guntime',
        'distance',
        'discipline',
        'event_format',
        'isvirtual',
        'imageupload',
        'hyperlink',
        'verifiedresultforvirtual',
        'linkedathlete',
        'athlete_type'
    )

    ordering = ('eventinstance',)


admin.site.register(Result, ResultsAdmin)
