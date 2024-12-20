from django.contrib import admin

# Register your models here.
from .models import Team, Person, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    list_display =["imie", "nazwisko"]
    readonly_fields = ["data_dodania"]


admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)