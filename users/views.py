from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import User, Pairs
from rounds.forms import NewPairForm
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


def add(request):
    users = User.objects.all()

    if request.method == 'POST':
        form = NewPairForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('pairs/save/')

    else:
        form = NewPairForm()

    return render(request, 'add_pair.html', {'users': users})


def save(request):
    first_user_id = request.POST.get('first_user_id')
    second_user_id = request.POST.get('second_user_id')

    Pairs(first_user_id=first_user_id, second_user_id=second_user_id).save()

    return HttpResponseRedirect('/users/pairs/add/')
    # Pairs.objects.create(first_user_id=first_user_id, second_user_id=second_user_id, meet_happened=True).save()

