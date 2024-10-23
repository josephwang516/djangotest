# polls/views.py

from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

# This view renders the index page with links to polls and persons
def index(request):
    return render(request, 'polls/index.html')  # Render the index template

# This view fetches all Person objects and renders them in a template
def person_list(request):
    persons = Person.objects.all()  # Fetch all Person objects from the database
    return render(request, 'polls/person_list.html', {'persons': persons})  # Render the template with context
