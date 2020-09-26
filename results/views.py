from django.shortcuts import render
from .models import Result
# Create your views here.

def all_results(request):
    """ A view to show all results, including sorting and search queries """

    results = Result.objects.all()

    context = {
        'results': results,
    }

    return render(request, 'results/results.html', context)