from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Round
from .forms import PairForm
from users.models import User, Pairs

import json


def make_round():
    users = User.objects.all()
    participants = users.filter(is_included=1)
    dated_pairs = Pairs.objects.all()

    next_round = []
    for user in participants:
        next_round.append(user)

    result = []
    amount_of_loops = len(next_round) // 2
    i = 0
    while i <= amount_of_loops:

        if next_round:
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
                result.append([first_user, second_user])
                #add to pairs here
                next_round.remove(second_user)
            else:
                result.append([first_user, users.filter(first_name = 'Анна', second_name = 'Махнева')])

        i += 1

    return result

def get_round(request, round_id):
    round_json = Round.objects.get(id=round_id).participants
    round = json.loads(round_json)

    return render(request, "round.html", {"round": round})


def validate_round(request):
    round = make_round()

    if request.method == 'POST':
        form = PairForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('save')

    else:
        form = PairForm()


    return render(request, 'validate_pairs.html', {'form': form, 'round': round})

def save(request):
    first_user_ids = request.POST.getlist('first_user')
    second_user_ids = request.POST.getlist('second_user')
    starts_at = request.POST.get('starts_at')
    ends_at = request.POST.get('ends_at')

    pairs_count = len(first_user_ids) - 1

    round = []
    i = 0
    while i <= pairs_count:
        first_user = User.objects.get(id=first_user_ids[i])
        second_user = User.objects.get(id=second_user_ids[i])

        Pairs(first_user_id=first_user_ids[i], second_user_id=second_user_ids[i], meet_happened=1).save()
        round.append(
            first_user.first_name + ' ' + first_user.second_name
            + ' - ' +
            second_user.first_name + ' ' + second_user.second_name
        )
        i += 1

    Round(participants=json.dumps(round), starts_at=starts_at, ends_at=ends_at).save()
    round_id = (Round.objects.last()).id

    return HttpResponseRedirect('/rounds/{:n}'.format(round_id))
