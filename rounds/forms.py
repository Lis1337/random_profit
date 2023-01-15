from django import forms


class PairForm(forms.Form):
    first_user = forms.CharField(label='first_user', max_length=100)
    second_user = forms.CharField(label='second_user', max_length=100)
    starts_at = forms.DateField()
    ends_at = forms.DateField()


class NewPairForm(forms.Form):
    first_user_id = forms.IntegerField(label='first_user_id')
    second_user_id = forms.IntegerField(label='second_user_id')
    # meet_happened = forms.BooleanField(label='meet_happened')
