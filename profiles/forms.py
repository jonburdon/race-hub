from django import forms
from .models import UserProfile, RaceHubFriends, NonRaceHubFriends, AthleteProfile
from clubs.models import Club
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from bootstrap_datepicker.widgets import DatePicker

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            self.fields[field].label = False



class AthleteProfileForm(forms.ModelForm):
    class Meta:
        model = AthleteProfile
        exclude = ('user','eaverified', 'userprofile')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['dateofbirth'] = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
        )

        placeholders = {
            'club': 'Club',
            'athletefirstname': 'First Name',
            'athletesurname': 'Surname',
            'eanumber': 'England Athletics Number',
            'emergencycontactname': 'Emergency Contact Name',
            'emergencycontactphone': 'Emergency Contact Phone',
            'gender': 'Gender',
            'tshirtsize': 'T Shirt Size',
            
        }

        for field in self.fields:
            if field != 'dateofbirth':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'requiredField border-black rounded-0 profile-form-input'
            
           


class AddRacehubFriendForm(forms.ModelForm):
    class Meta:
        model = RaceHubFriends
        fields = (
        'myfriendsracehubid',
        
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
       
        for field_name, field in self.fields.items():

                
            field.widget.attrs['class'] = 'border-black rounded-0'

        




class FamilyandFriendsForm(forms.ModelForm):

    class Meta:
        model = NonRaceHubFriends
        exclude = ('parentprofile', 'eaverified', 'entrycutoff')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        clubs = Club.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in clubs]
        
        self.fields['dateofbirth'] = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
        )
        self.fields['club'].choices = friendly_names
        #self.fields['format'].choices = friendly_namesformat
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'skew-style border-black rounded-0'


