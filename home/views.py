from django.shortcuts import render
from events.models import Event, EventInstance
# Create your views here.

def index(request):
    """ A view to return the index page """

    events = Event.objects.all()
    eventinstances = EventInstance.objects.all()[:3]
    
    context = {
        'events': events,
    }

    return render(request, 'home/index.html', context)