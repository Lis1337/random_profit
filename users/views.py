from django.http import HttpResponse
from django.shortcuts import render

from .models import User, Round, Pairs



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
    for first_user in participants:
        for second_user in participants:

            first_user_concatenated_name = first_user.first_name + '_' + first_user.second_name
            second_user_concatenated_name = second_user.first_name + '_' + second_user.second_name

            first_dated_pair_exists = dated_pairs.filter(
                first_user=first_user_concatenated_name, 
                second_user=second_user_concatenated_name
                ).exists()
            second_dated_pair_exists = dated_pairs.filter(
                first_user=second_user_concatenated_name, 
                second_user=first_user_concatenated_name
                ).exists()

            first_pair = [
                first_user_concatenated_name, 
                second_user_concatenated_name
                ]
            second_pair = [
                second_user_concatenated_name, 
                first_user_concatenated_name
                ]

            pair_string = first_user_concatenated_name + ':' + second_user_concatenated_name
            pair_string_reversed = second_user_concatenated_name + ':' + first_user_concatenated_name

            if (
                (first_user != second_user) and
                ((not first_dated_pair_exists) and (not second_dated_pair_exists)) and 
                ((first_pair not in next_round) and (second_pair not in next_round)) and
                (pair_string not in next_round and pair_string_reversed not in next_round)
            ):
                next_round.append(pair_string)


    return render(request, 'base.html', {"round": next_round})


def add_is_possible(next_round: list) -> bool:
    possible = False



    return possible