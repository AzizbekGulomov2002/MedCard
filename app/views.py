from django.shortcuts import render
from django.views.generic import ListView
from .models import MedCard, Logo


def index(request):
    medcard = MedCard.objects.all()
    logo = Logo.objects.all()
    
    contex = {
        'MedCard':medcard,
        'Logo':logo,

    }
    return render(request, ['index.html'] , contex)


def main(request):
    medcard = MedCard.objects.all()
    contex = {
        'MedCard':medcard,
    }
    return render(request, ['main.html'] , contex)