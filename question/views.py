from django.shortcuts import render

# Create your views here.


def index_view(request):
    html = 'index.html'
    return render(request, html, {'key': 'value'})
