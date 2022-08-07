from django.http import HttpResponse
from django.shortcuts import render

from .models import User, Round, Pairs
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


def make_round(request):
    users = User.objects.all()
    participants = users.filter(is_included=1)
    dated_pairs = Pairs.objects.all()

    next_round = []
    for user in participants:
        next_round.append(user.first_name + '_' + user.second_name)

    result = []
    amount_of_loops = len(next_round) // 2
    i = 0
    while i <= amount_of_loops:

        first_user = next_round.pop()
        second_user = None

        for second in next_round:
            pairs_exists = (
                dated_pairs.filter(first_user=first_user, second_user=second).exists() or
                dated_pairs.filter(first_user=second, second_user=first_user).exists()
            )

            if ((first_user != second) and (not pairs_exists)):
                second_user = second
                break


        if ((second_user is not None) and (first_user != second_user)):
            result.append(first_user + ':' + second_user)
            next_round.remove(second_user)
        else:
            result.append(first_user + ':' + 'Ann_Machneva')

        i += 1



    return render(request, 'base.html', {"round": result,})
