from django import forms
from .widgets import CustomClearableFileInput
from .models import Event, Discipline, Distance, Format, Organiser


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

        self.fields['discipline'].choices = friendly_names
        self.fields['distance'].choices = friendly_namesdist
        self.fields['organiser'].choices = friendly_namesorganiser
        #self.fields['format'].choices = friendly_namesformat
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'