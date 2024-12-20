from django.urls import path

# importujemy moduł views (plik views.py z tego samego katalogu co plik bieżący)
from . import views

# definiujemy zmienną urlpatterns, która jest listą mapowań adresów URL na nasze widoki
urlpatterns = [
    path("welcome", views.welcome_view),
    path("persons", views.person_list),
    path("person/<int:id>", views.person_detail),
    path('team/<int:id>/', views.team_detail, name='team_detail'),
    path('teams/', views.team_list, name='team_list'),
]