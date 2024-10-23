from django.urls import path
from . import views


# polls/urls.py

from django.urls import path
from .views import index, person_list  # Import the view functions

urlpatterns = [
    path('', index, name='index'),  # Maps the root URL to the index view
    path('persons/', person_list, name='person_list'),  # Maps /persons/ to the person_list view
]
