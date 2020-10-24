from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Result
from events.models import EventInstance
from clubs.models import Club
from .forms import ResultForm, FullResultForm, TimeOnlyResultForm, EntryTransferForm
from .admin import ResultDownload
import csv
from io import StringIO
from django.core.mail import EmailMessage
# Create your views here.

def all_result_lists(request):
    """ A view to show all event_instances including sorting and search queries """

    resultlists = EventInstance.objects.all()
    query = None
    name = None
    agecat = None
    chiptime = None
    guntime = None
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
            queries = Q(friendlyname__icontains=query)
            resultlists = resultlists.filter(queries)  

    current_sorting = f'{sort}_{direction}'

    context = {
        'resultlists': resultlists,
        'current_sorting': current_sorting,
    }
    
    return render(request, 'results/result_lists.html', context)

def single_event_result_list(request, eventinstance_id):
    """ A view to show result list for one event """

    eventinstance = get_object_or_404(EventInstance, pk=eventinstance_id)
    results = Result.objects.all()
    resultsforthisevent = results.filter(eventinstance=eventinstance)
    query = None
    name = None
    agecat = None
    gender = None
    chiptime = None
    guntime = None
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
            if sortkey == 'guntime':
                sortkey = 'guntime'
            if sortkey == 'club':
                sortkey = 'club__name'
            if sortkey == 'athletesurname':
                sortkey = 'athletesurname'
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
            queries = Q(athletesurname__icontains=query) | Q(athletefirstname__icontains=query) | Q(agecat__icontains=query)  | Q(club__friendly_name__icontains=query)
            resultsforthisevent = resultsforthisevent.filter(queries)  

    current_sorting = f'{sort}_{direction}'

    context = {
        'eventinstance': eventinstance,
        'resultsforthisevent' : resultsforthisevent,
        'search_term': query,
        'current_agecat' : agecat,
        'current_gender' : gender,
        'current_sorting': current_sorting,
    }

    return render(request, 'results/single_result_list.html', context)


def review_virtual_results(request, eventinstance_id):
    """ A view to show result list for one event """

    eventinstance = get_object_or_404(EventInstance, pk=eventinstance_id)
    results = Result.objects.all()
    resultsforthisevent = results.filter(eventinstance=eventinstance)
    query = None
    name = None
    agecat = None
    gender = None
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
            if sortkey == 'athletesurname':
                sortkey = 'athletesurname'
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
            queries = Q(athletesurname__icontains=query) | Q(athletefirstname__icontains=query) | Q(agecat__icontains=query)  | Q(club__friendly_name__icontains=query)
            resultsforthisevent = resultsforthisevent.filter(queries)  

    current_sorting = f'{sort}_{direction}'

    context = {
        'eventinstance': eventinstance,
        'resultsforthisevent' : resultsforthisevent,
        'search_term': query,
        'current_agecat' : agecat,
        'current_gender' : gender,
        'current_sorting': current_sorting,
    }

    return render(request, 'results/review_virtual_results.html', context)

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
            if sortkey == 'guntime':
                sortkey = 'guntime'
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
            queries = Q(athletefirstname__icontains=query) | Q(athletesurname__icontains=query) | Q(agecat__icontains=query)  | Q(club__friendly_name__icontains=query)
            results = results.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'results': results,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'results/results.html', context)

def single_result(request, result_id):
    """ A view to show single details """

    result = get_object_or_404(Result, pk=result_id)

    context = {
        'result': result,
    }

    return render(request, 'results/single_result.html', context)

@login_required
def add_result(request, eventinstance_id):
    """ Add a result to the database """
    eventinstance = eventinstance_id
    if request.method == 'POST':
        form = ResultForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added result!')
            return redirect(reverse('add_result', args=[eventinstance]))
        else:
            messages.error(request, 'Failed to add result. Please ensure the form is valid.')
    else:
        form = ResultForm()
        
    template = 'results/add_result.html'
    context = {
        'eventinstance': eventinstance_id,
        'form': form,
    }
    return render(request, 'results/add_result.html', context)
    #return render(request, template, context)

def result_detail(request, result_id):
    """ A view to show individual result details """
    result = get_object_or_404(Result, pk=result_id)
    context = {
        'result': result,
    }
    return render(request, 'results/result_detail.html', context)


@login_required
def edit_full_result(request, result_id):
    """ Edit a result in the results system """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    result = get_object_or_404(Result, pk=result_id)
    if request.method == 'POST':
        form = FullResultForm(request.POST, request.FILES, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated result!')
            return redirect(reverse('single_result', args=[result.id]))
        else:
            messages.error(request, 'Failed to update result. Please ensure the form is valid.')
    else:
        form = FullResultForm(instance=result)
        messages.info(request, f'You are editing {result.eventinstance.friendlyname}')

    template = 'results/edit_full_result.html'
    context = {
        'form': form,
        'result': result,
    }

    return render(request, template, context)


@login_required
def edit_result_time_only(request, result_id):
    """ Edit a time in the results system - use for virtual events for this athlete """

    result = get_object_or_404(Result, pk=result_id)
    
    if request.method == 'POST':
        form = TimeOnlyResultForm(request.POST, request.FILES, instance=result)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated result!')
            return redirect(reverse('single_result', args=[result.id]))
        else:
            messages.error(request, 'Failed to update result. Please ensure the form is valid.')
    else:
        form = TimeOnlyResultForm(instance=result)
        messages.info(request, f'You are editing {result.eventinstance.friendlyname}')

    template = 'results/edit_time_only_for_result.html'
    context = {
        'form': form,
        'result': result,
    }

    return render(request, template, context)

@login_required
def transfer_result(request, result_id):
    """ Transfer a result in the results system """

    result = get_object_or_404(Result, pk=result_id)
    if request.method == 'POST':
        form = EntryTransferForm(request.POST, request.FILES, instance=result)
        if form.is_valid():
            #need to ensure eventid is changed
            form.save()
            messages.success(request, 'Successfully updated result!')
            return redirect(reverse('single_result', args=[result.id]))
        else:
            messages.error(request, 'Failed to update result. Please ensure the form is valid.')
    else:
        form = EntryTransferForm(instance=result)
        messages.info(request, f'You are editing your entry for{result.eventinstance.friendlyname}')

    template = 'results/transfer_full_result.html'
    context = {
        'form': form,
        'result': result,
    }

    return render(request, template, context)


def download_results(request):
    dataset = ResultDownload().export()
    email = EmailMessage(
            'Subject',
            'Body',
            'jon@branchoutwebsites.com',
            ['jon@branchoutwebsites.com'],
        )
    email.attach('dataset.csv', dataset.csv)
    email.send()

    messages.info(request, 'Download complete - this will be emailed')

    template = 'results/result_download.html'

    return render(request, template )

@login_required
def verify_result(request, result_id):
    """ Verify a result is genuine """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    result = get_object_or_404(Result, pk=result_id)
    result.verifiedresultforvirtual = True
    result.save()
    messages.success(request, 'Result Verified!')
    return redirect(reverse('single_result', args=[result.id]))

@login_required
def unverify_result(request, result_id):
    """ Unverify a result is genuine """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    result = get_object_or_404(Result, pk=result_id)
    result.verifiedresultforvirtual = False
    result.save()
    messages.success(request, 'Result Unverified!')
    return redirect(reverse('single_result', args=[result.id]))

@login_required
def delete_result(request, result_id):
    """ Delete an result from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    result = get_object_or_404(Result, pk=result_id)
    eventinstance = result.eventinstance.id
    result.delete()
    messages.success(request, 'Result deleted!')
    
    return redirect(reverse('single_event_result_list', args=[eventinstance]))