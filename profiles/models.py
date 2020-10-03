from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from clubs.models import Club

from django_countries.fields import CountryField




class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username

class AthleteProfile(models.Model):
    """
    A user profile model for maintaining athlete data and club memberships
    """
    athletefirstname = models.CharField(max_length=60, null=True, blank=True)
    athletesurname = models.CharField(max_length=60, null=True, blank=True)
    eanumber = models.CharField(max_length=80, null=True, blank=True)
    eaverified = models.BooleanField(default=True)
    club = models.ForeignKey(Club, null=True, blank=True, on_delete=models.SET_NULL)
    dateofbirth  = models.DateField( null=True, blank=True )
    emergencycontactname = models.CharField(max_length=60, null=True, blank=True)
    emergencycontactphone = models.CharField(max_length=20, null=True, blank=True)
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
        null=True, blank=True
    )
    Small = 'Small'
    Medium = 'Med'
    Large = 'Large'
    tshirtsize_choices = [
        (Small, 'Small'),
        (Medium, 'Medium'),
        (Large, 'Large'),
    ]
    tshirtsize = models.CharField(
        max_length=5,
        choices=tshirtsize_choices,
        default=Medium
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username


class RaceHubFriends(models.Model):
    """
    Selected Racehub Friends to be available for entering.
    """
    rfuserprofile = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    rfathleteprofile = models.ForeignKey(AthleteProfile, null=True, blank=True, on_delete=models.SET_NULL)
    myfriendsracehubid = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    


class NonRaceHubFriends(models.Model):
    """
    Selected NON RACEHUB Friends and Family to be entered for events.
    """
    parentprofile = models.ForeignKey(AthleteProfile, on_delete=models.CASCADE)
    athletefirstname = models.CharField(max_length=60, null=True, blank=True)
    athletesurname = models.CharField(max_length=60, null=True, blank=True)
    eanumber = models.CharField(max_length=80, null=True, blank=True)
    eaverified = models.BooleanField(default=True)
    club = models.ForeignKey(Club, null=True, blank=True, on_delete=models.SET_NULL)
    dateofbirth  = models.DateField( null=True, blank=True )
    emergencycontactname = models.CharField(max_length=60, null=True, blank=True)
    emergencycontactphone = models.CharField(max_length=20, null=True, blank=True)
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
        null=True, blank=True
    )
    Small = 'Small'
    Medium = 'Med'
    Large = 'Large'
    tshirtsize_choices = [
        (Small, 'Small'),
        (Medium, 'Medium'),
        (Large, 'Large'),
    ]
    tshirtsize = models.CharField(
        max_length=5,
        choices=tshirtsize_choices,
        default=Medium
    )

   


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()

