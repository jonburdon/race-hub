from django.db import models
from events.models import Event, EventInstance, Organiser, Format, Distance, Discipline
from clubs.models import Club
# Create your models here.


class Result(models.Model):
    eventinstance = models.ForeignKey(EventInstance, on_delete=models.SET_NULL, null=True)
    distance = models.ForeignKey(Distance, null=True, blank=True, on_delete=models.SET_NULL)
    discipline = models.ForeignKey(Discipline, null=True, blank=True, on_delete=models.SET_NULL)
    event_format = models.ForeignKey(Format, null=True, blank=True, on_delete=models.SET_NULL)
    athletefirstname = models.CharField(max_length=40, null=True)
    athletesurname = models.CharField(max_length=40, null=True)
    athlete = models.CharField(max_length=125, null=True, blank=True)
    dateofbirth = models.DateField(null=True, blank=True)
    M = 'M'
    F = 'F'
    N = 'N'
    gender_choices = [
        (M, 'M'),
        (F, 'F'),
        (N, 'Prefer not to say'),
    ]
    gender = models.CharField(
        max_length=2,
        choices=gender_choices,
        null=True
    )

    bibnumber = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)
    Junior = 'Jr'
    Senior = 'Snr'
    V35 = 'V35'
    V40 = 'V40'
    V45 = 'V45'
    V50 = 'V50'
    V55 = 'V55'
    V60 = 'V60'
    V65 = 'V65'
    V70 = 'V70'
    V75 = 'V75'
    V80 = 'V80'
    age_cat_choices = [
        (Junior, 'Junior'),
        (Senior, 'Senior'),
        (V35, 'V35'),
        (V40, 'V40'),
        (V45, 'V45'),
        (V50, 'V50'),
        (V55, 'V55'),
        (V60, 'V60'),
        (V65, 'V65'),
        (V70, 'V70'),
        (V75, 'V75'),
        (V80, 'V80'),
    ]
    agecat = models.CharField(
        max_length=6,
        choices=age_cat_choices,
        default=Senior,
        null=True, blank=True
    )
    Myself = 'myself'
    NonRacehubFriend = 'nonracehubfriend'
    RacehubFriend = 'racehubfriend'
    athlete_type_choices = [
        (Myself, 'Myself'),
        (NonRacehubFriend, 'Friends or Family'),
        (RacehubFriend, 'Racehub Friend'),
    ]
    athlete_type = models.CharField(
        max_length=18,
        choices=athlete_type_choices,
        default=Myself,
        null=True, blank=True
    )
    club = models.ForeignKey(Club, null=True, blank=True, on_delete=models.SET_NULL)
    chiptime = models.DurationField(null=True, blank=True)
    guntime = models.DurationField(null=True, blank=True)
    isvirtual = models.BooleanField(null=True, blank=True, default=False)
    hyperlink = models.CharField(max_length=240, null=True, blank=True)
    imageupload = models.ImageField(null=True, blank=True)
    verifiedresultforvirtual = models.BooleanField(null=True, blank=True, default=False)
    linkedathlete = models.DecimalField(max_digits=3, decimal_places=0, null=True, blank=True)

