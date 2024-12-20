from django.db import models

# Create your models here.

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

PLEC = models.IntegerChoices("Płeć", "Kobieta mężczyzna inne")
SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)
    website = models.URLField(null=True)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Choose your team")
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Stanowisko(models.Model):
    nazwa=models.CharField(max_length=50)
    opis= models.TextField(null=True, blank=True)

class Osoba(models.Model):
    imie = models.CharField(max_length=60, blank=False)
    nazwisko = models.CharField(max_length=60, blank=False)
    plec = models.IntegerField(choices=PLEC.choices, default=PLEC.choices[0][0])
    Stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Osoba"

