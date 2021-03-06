from django import forms
from .widgets import CustomClearableFileInput
from .models import Event, Discipline, Distance, Format, Organiser, EventInstance
from bootstrap_datepicker.widgets import DatePicker

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disciplines = Discipline.objects.all()
        distances = Distance.objects.all()
        formats = Format.objects.all()
        organisers = Organiser.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in disciplines]
        friendly_namesdist = [(c.id, c.get_friendly_name()) for c in distances]
        friendly_namesformat = [(c.id, c.get_friendly_name()) for c in formats]
        friendly_namesorganiser = [(c.id, c.get_friendly_name()) for c in organisers]
        self.fields['entrycutoff'] = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )
        self.fields['discipline'].choices = friendly_names
        self.fields['distance'].choices = friendly_namesdist
        self.fields['organiser'].choices = friendly_namesorganiser
        #self.fields['format'].choices = friendly_namesformat
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class EventInstanceForm(forms.ModelForm):

    class Meta:
        model = EventInstance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.fields['eventdate'] = forms.DateField(
        widget=forms.TextInput(
            attrs={'type': 'date'}
        )
    )

        #self.fields['format'].choices = friendly_namesformat
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class EventAndInstanceConnectForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = (

        'event_instance',
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class PostcodeForm(forms.Form):
    postcode = forms.CharField(label='Postcode', max_length=10)
    class Meta:
        fields = (
        'postcode',
    )
    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)

    #for field_name, field in self.fields.items():
    #    field.widget.attrs['class'] = 'border-black rounded-0'