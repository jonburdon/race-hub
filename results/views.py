from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Result
# Create your views here.

def all_results(request):
    """ A view to show all results, including sorting and search queries """

    results = Result.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('results'))
            
            queries = Q(athlete__icontains=query) | Q(agecat__icontains=query)
            results = results.filter(queries)

    context = {
        'results': results,
        'search_term': query,
    }

    return render(request, 'results/results.html', context)