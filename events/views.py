from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Event, Discipline, Distance, Format
from profiles.models import AthleteProfile, RaceHubFriends, NonRaceHubFriends

from .forms import EventForm
# Create your views here.

def all_events(request):
    """ A view to show all events, including sorting and search queries """

    events = Event.objects.all()
    query = None
    disciplines = None
    distances = None
    exactdistancekm = None
    event_format = None
    sort = None
    direction = None
    formats = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower('name'))
            if sortkey == 'discipline':
                sortkey = 'discipline__name'
            if sortkey == 'exactdistancekm':
                sortkey = 'exactdistancekm'
            if sortkey == 'format':
                sortkey = 'format__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            events = events.order_by(sortkey)



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

    current_sorting = f'{sort}_{direction}'

    context = {
        'events': events,
        'search_term': query,
        'current_disciplines': disciplines,
        'current_distance': distances,
        'current_format': formats,
        'current_sorting': current_sorting,
 
    }

    return render(request, 'events/events.html', context)


def event_profile(request, event_id):
    """ A view to show individual event details """
    
    if request.user.is_authenticated:
        athleteprofile = get_object_or_404(AthleteProfile, user=request.user)
        event = get_object_or_404(Event, pk=event_id)
        racehubfriends = RaceHubFriends.objects.all()
        racehubfriendsforthisathlete = racehubfriends.filter(rfathleteprofile_id=athleteprofile.id)
        racehubfriendprofiles = AthleteProfile.objects.all()

        nonracehubfriends = NonRaceHubFriends.objects.all()
        nonracehubfriendsforthisathlete = nonracehubfriends.filter(parentprofile_id=athleteprofile.id)

        context = {
            'event': event,
            'athleteprofile': athleteprofile,
            'racehubfriendprofiles': racehubfriendprofiles,
            'racehubfriendsforthisathlete': racehubfriendsforthisathlete,
            'nonracehubfriendsforthisathlete': nonracehubfriendsforthisathlete,
        }

        return render(request, 'events/event_profile.html', context)

    else:
        event = get_object_or_404(Event, pk=event_id)
        context = {'event': event}
        return render(request, 'events/event_profile_notloggedin.html', context)

    



def map_view(request):
    """ A view to show all events on a map """

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'events/map_view.html', context)

@login_required
def add_event(request):
    """ Add an event to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event=form.save()
            messages.success(request, 'Successfully added event!')
            return redirect(reverse('event_profile', args=[event.id]))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventForm()


    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_event(request, event_id):
    """ Edit an event in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('event_profile', args=[event.id]))
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.name}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)

@login_required
def delete_event(request, event_id):
    """ Delete an event from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))