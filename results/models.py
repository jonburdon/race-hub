from django.db import models
from events.models import Event, EventInstance, Organiser, Format, Distance, Discipline

from clubs.models import Club
# Create your models here.


class Result(models.Model):
    eventinstance = models.ForeignKey(EventInstance, on_delete=models.SET_NULL, null=True, blank=True)
    distance = models.ForeignKey(Distance, null=True, blank=True, on_delete=models.SET_NULL)
    discipline = models.ForeignKey(Discipline, null=True, blank=True, on_delete=models.SET_NULL)
    event_format = models.ForeignKey(Format, null=True, blank=True, on_delete=models.SET_NULL)
    athlete = models.CharField(max_length=125, null=True, blank=True)
    M = 'M'
    F = 'M'
    N = 'N'
    gender_choices = [
        (M, 'M'),
        (F, 'F'),
        (N, 'Prefer not to say'),
    ]
    gender = models.CharField(
        max_length=2,
        choices=gender_choices,
        null=True, blank=True
    )

    bibnumber = models.DecimalField(max_digits=6, decimal_places=0)
    Junior = 'Jr'
    Senior = 'Snr'
    Veteran = 'Vet'
    age_cat_choices = [
        (Junior, 'Junior'),
        (Senior, 'Senior'),
        (Veteran, 'Vet'),
    ]
    agecat = models.CharField(
        max_length=6,
        choices=age_cat_choices,
        default=Senior,
        null=True, blank=True
    )
    club = models.ForeignKey(Club, null=True, blank=True, on_delete=models.SET_NULL)
    chiptime = models.DurationField(null=True, blank=True)
    guntime = models.DurationField(null=True, blank=True)



    def __str__(self):
        return self.athlete