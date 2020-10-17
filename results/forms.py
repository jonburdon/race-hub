from django import forms
from .models import Result
from bootstrap_datepicker.widgets import DatePicker
from clubs.models import Club
from events.models import EventInstance

class ResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = (
        'eventinstance',
        'athletefirstname',
        'athletesurname',
        'bibnumber',
        'gender',
        'dateofbirth',
        'club',
        'chiptime',
        'guntime',
        'linkedathlete',
        'athlete_type',
        'isvirtual',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        clubs = Club.objects.all()
        events = EventInstance.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in clubs]
        
        self.fields['club'].choices = friendly_names
        self.fields['dateofbirth'] = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
        )
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class FullResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        clubs = Club.objects.all()
        events = EventInstance.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in clubs]
        
        self.fields['club'].choices = friendly_names
        self.fields['dateofbirth'] = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
        )
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class TimeOnlyResultForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = (
        'chiptime',
        'hyperlink',
        'imageupload',

    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'



class EntryTransferForm(forms.ModelForm):

    class Meta:
        model = Result
        fields = (
        'eventinstance',
        'athletefirstname',
        'athletesurname',
        'gender',
        'dateofbirth',
        'club',
        'agecat',
        'athlete_type',
        'linkedathlete'
    )

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        clubs = Club.objects.all()
        events = EventInstance.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in clubs]
        
        self.fields['club'].choices = friendly_names

        self.fields['dateofbirth'] = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
        )
       
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'