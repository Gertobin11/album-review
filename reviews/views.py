from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    name = request.GET.get('name') or "world"
    context = {
        'name': name
    }
    template = 'index.html'
    return render(request, template, context)

def search_results(request):
    if request.method == 'POST':
        return
    else:
        context = {}
        template = 'search_results.html'
        return render(request, template, context)