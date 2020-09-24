from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Event, Discipline, Distance, Format
# Create your views here.

def all_events(request):
    """ A view to show all events, including sorting and search queries """

    events = Event.objects.all()

    query = None
    disciplines = None
    distances = None
    event_format = None

    if request.GET:
        if 'discipline' in request.GET:
            discipline = request.GET['discipline'].split(',')
            events = events.filter(discipline__name__in=discipline)
            disciplines = Discipline.objects.filter(name__in=discipline)

        if 'distance' in request.GET:
            distance = request.GET['distance'].split(',')
            events = events.filter(distance__name__in=distance)
            distances = Distance.objects.filter(name__in=distance)

        if 'event_format' in request.GET:
            event_format = request.GET['event_format'].split(',')
            events = events.filter(event_format__name__in=event_format)
            formats = Format.objects.filter(name__in=event_format)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('events'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            events = events.filter(queries)


    context = {
        'events': events,
        'search_term': query,
        'current_disciplines': disciplines,
        'current_distance': distances,
        'current_format': event_format,
    }

    return render(request, 'events/events.html', context)

def event_profile(request, event_id):
    """ A view to show individual event details """

    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'events/event_profile.html', context)