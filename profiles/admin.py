from django.contrib import admin
from django.contrib.auth.models import User
from .models import AthleteProfile, UserProfile, RaceHubFriends, NonRaceHubFriends
from clubs.models import Club

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
    'user',
    'default_phone_number', 
    'default_street_address1', 
    'default_street_address2', 
    'default_town_or_city', 
    'default_county', 
    'default_postcode', 
    'default_country', 
    )

class AthleteProfileAdmin(admin.ModelAdmin):
    list_display = (
    'eanumber',
    'eaverified',
    'club',
    'dateofbirth',
    'emergencycontactname',
    'emergencycontactphone',
    'gender', 
    'tshirtsize', 
    'user',
    'userprofile',
    )

class NonRaceHubFriendsAdmin(admin.ModelAdmin):
    list_display = (
    'athletefirstname',
    'athletesurname',
    'parentprofile',
    'eanumber',
    'eaverified',
    'club',
    'dateofbirth',
    'emergencycontactname',
    'emergencycontactphone',
    'gender', 
    'tshirtsize', 
    )

class RaceHubFriendsAdmin(admin.ModelAdmin):
    list_display = (
    'rfuserprofile',
    'rfathleteprofile',
    'myfriendsracehubid',
    )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AthleteProfile, AthleteProfileAdmin)
admin.site.register(RaceHubFriends, RaceHubFriendsAdmin)
admin.site.register(NonRaceHubFriends, NonRaceHubFriendsAdmin)