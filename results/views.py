from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Result
from events.models import EventInstance
from clubs.models import Club
# Create your views here.

def all_result_lists(request):
    """ A view to show all event_instances including sorting and search queries """

    resultlists = EventInstance.objects.all()
    query = None
    name = None
    agecat = None
    chiptime = None
    club = None
    athlete = None
    sort = None
    events = None
    direction = None
    bibnumber = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower('name'))
            if sortkey == 'agecat':
                sortkey = 'agecat'
            if sortkey == 'chiptime':
                sortkey = 'chiptime'
            if sortkey == 'club':
                sortkey = 'club_name'
            if sortkey == 'athlete':
                sortkey = 'athlete'
            if sortkey == 'bibnumber':
                sortkey = 'bibnumber'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            resultlists = resultlists.order_by(sortkey)

        if 'agecat' in request.GET:
            agecat = request.GET['agecat'].split(',')
            resultlists = resultlists.filter(agecat__in=agecat)
            agecat = Result.objects.filter(agecat__in=agecat)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            resultlists = resultlists.filter(gender__in=gender)
            gender = Result.objects.filter(gender__in=gender)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('results'))
            queries = Q(event__friendly_name__icontains=query)
            resultlists = resultlists.filter(queries)  

    context = {
        'resultlists': resultlists,
    }
    
    return render(request, 'results/result_lists.html', context)

def single_event_result_list(request, eventinstance_id):
    """ A view to show result list for one event """

    eventinstance = get_object_or_404(EventInstance, pk=eventinstance_id)
    
    results = Result.objects.all()
    resultsforthisevent = results.filter(eventinstance__in=eventinstance_id)
    query = None
    name = None
    agecat = None
    chiptime = None
    club = None
    athlete = None
    sort = None
    direction = None
    bibnumber = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower('name'))
            if sortkey == 'agecat':
                sortkey = 'agecat'
            if sortkey == 'chiptime':
                sortkey = 'chiptime'
            if sortkey == 'club':
                sortkey = 'club__name'
            if sortkey == 'athlete':
                sortkey = 'athlete'
            if sortkey == 'bibnumber':
                sortkey = 'bibnumber'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            resultsforthisevent = resultsforthisevent.order_by(sortkey)

        if 'agecat' in request.GET:
            agecat = request.GET['agecat'].split(',')
            resultsforthisevent = resultsforthisevent.filter(agecat__in=agecat)
            agecat = Result.objects.filter(agecat__in=agecat)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            resultsforthisevent = resultsforthisevent.filter(gender__in=gender)
            gender = Result.objects.filter(gender__in=gender)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('results'))
            queries = Q(athlete__icontains=query) | Q(agecat__icontains=query)  | Q(club__friendly_name__icontains=query)
            resultsforthisevent = resultsforthisevent.filter(queries)  

    context = {
        'eventinstance': eventinstance,
        'resultsforthisevent' : resultsforthisevent,
    }

    return render(request, 'results/single_result_list.html', context)

def all_results(request):
    """ A view to show all results, including sorting and search queries """

    results = Result.objects.all()
    query = None
    name = None
    agecat = None
    chiptime = None
    club = None
    athlete = None
    sort = None
    direction = None
    bibnumber = None


    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                events = events.annotate(lower_name=Lower('name'))
            if sortkey == 'agecat':
                sortkey = 'agecat'
            if sortkey == 'chiptime':
                sortkey = 'chiptime'
            if sortkey == 'club':
                sortkey = 'club__name'
            if sortkey == 'athlete':
                sortkey = 'athlete'
            if sortkey == 'bibnumber':
                sortkey = 'bibnumber'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            results = results.order_by(sortkey)

        if 'agecat' in request.GET:
            agecat = request.GET['agecat'].split(',')
            results = results.filter(agecat__in=agecat)
            agecat = Result.objects.filter(agecat__in=agecat)

        if 'gender' in request.GET:
            gender = request.GET['gender'].split(',')
            results = results.filter(gender__in=gender)
            gender = Result.objects.filter(gender__in=gender)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('results'))
            queries = Q(athlete__icontains=query) | Q(agecat__icontains=query)  | Q(club__friendly_name__icontains=query)
            results = results.filter(queries)

    context = {
        'results': results,
        'search_term': query,
    }

    return render(request, 'results/results.html', context)

def single_result(request, result_id):
    """ A view to show single details """

    result = get_object_or_404(Result, pk=result_id)

    context = {
        'result': result,
    }

    return render(request, 'results/single_result.html', context)