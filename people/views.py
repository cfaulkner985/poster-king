from django.shortcuts import render

# Create your views here.


def people(request):
    """ A view to return the people page """

    return render(request, '/people.html')
