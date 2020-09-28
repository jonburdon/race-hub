from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Distance(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Format(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Organiser(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class EventInstance(models.Model):
    name = models.CharField(max_length=254)
    friendlyname = models.CharField(max_length=254, null=True, blank=True)
    eventdate = models.DateTimeField()
    race_limit = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Event(models.Model):
    discipline = models.ForeignKey('Discipline', null=True, blank=True, on_delete=models.SET_NULL)
    distance = models.ForeignKey('Distance', null=True, blank=True, on_delete=models.SET_NULL)
    exactdistancekm = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    event_format = models.ForeignKey('Format', null=True, blank=True, on_delete=models.SET_NULL)
    organiser = models.ForeignKey('Organiser', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    event_instance = models.OneToOneField(EventInstance, on_delete=models.CASCADE, null=True, blank=True)
    entrycutoff = models.DateTimeField()
    keyinfo = models.TextField()
    description = models.TextField()
    location_post_code = models.TextField(max_length=8)
    latitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name