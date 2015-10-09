from django.shortcuts import render

from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.forms import MyModelSearchForm

def search(request):

    if request.GET:
        form = MyModelSearchForm(request.GET)
        if form.is_valid():
            results = form.get_result_queryset()
        else:
            results = []
    else:
        form = MyModelSearchForm()
        results = []


    return render_to_response(
        'search.html',
        RequestContext(request, {
            'form': form,
            'results': results,
        })
    )