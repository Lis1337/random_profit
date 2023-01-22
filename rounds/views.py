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
    users_with_no_pair = []
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

                if (first_user != second) and (not pairs_exists):
                    second_user = second
                    break

            if (second_user is not None) and (first_user != second_user):
                result.append([first_user, second_user])
                # add to pairs here
                next_round.remove(second_user)
            else:
                users_with_no_pair.append(first_user)
                # result.append([first_user, User.objects.get(id=64)]) добавление Ани Махнёвой

        i += 1

    # if len(users_with_no_pair) > 0:
    #     remainders = distribute_remainders(users_with_no_pair, dated_pairs)
    #     result += remainders

    return result, users_with_no_pair


def get_round(request, round_id):
    round_json = Round.objects.get(id=round_id).participants
    round = json.loads(round_json)

    return render(request, "round.html", {"round": round})


def validate_round(request):
    round, users_with_no_pair = make_round()

    if request.method == 'POST':
        form = PairForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('save')

    else:
        form = PairForm()

    return render(request, 'validate_pairs.html',
                  {
                      'form': form,
                      'round': round,
                      'users_with_no_pair': users_with_no_pair
                  })


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


def distribute_remainders(users_with_no_pair: list | None, dated_pairs):
    result = []
    no_pair_amount = len(users_with_no_pair)

    x = 0
    if no_pair_amount == 1:
        result.append([users_with_no_pair[x], User.objects.get(id=64)])

    elif no_pair_amount > 1:
        if (no_pair_amount % 2) == 0:
            for users in users_with_no_pair:
                if not dated_pairs.filter(first_user=users_with_no_pair[x],
                                          second_user=users_with_no_pair[x + 1]).exists():
                    result.append([users_with_no_pair[x], users_with_no_pair[x + 1]])

        if (no_pair_amount % 2) == 1:
            result.append([users_with_no_pair.pop(), User.objects.get(id=64)])

        while x <= no_pair_amount:
            if not dated_pairs.filter(first_user=users_with_no_pair[x], second_user=users_with_no_pair[x + 1]).exists():
                result.append([users_with_no_pair[x], users_with_no_pair[x + 1]])
            else:
                result.append([users_with_no_pair[x], User.objects.get(id=64)])
                result.append([users_with_no_pair[x + 1], User.objects.get(id=64)])

    return result
