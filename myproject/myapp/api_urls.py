from django.urls import path, include
from . import api_views

urlpatterns = [
    path('persons/', api_views.person_list),
    path('osoby/', api_views.osoba_list),
    path('persons/<int:pk>/', api_views.person_detail),
]