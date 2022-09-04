from django.http import HttpResponse
from django.shortcuts import render

from .models import User, Pairs
from rounds.models import Round
import random



def index(request):
    return HttpResponse('NASTYA ZHOPA')


def get_users_list(request):
    list = User.objects.all()
    return render(request, "list.html", {"list": list})


def get_rounds(request):
    rounds = Round.objects.all()
    return render(request, "rounds.html", {"rounds": rounds})


def get_pairs(request):
    pairs = Pairs.objects.all()
    return render(request, 'pairs.html', {"pairs": pairs})
