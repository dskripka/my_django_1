from django import forms


class AddTicketForm(forms.Form):
    fullname = forms.CharField(max_length=40)
    from_place = forms.CharField(max_length=50)
    to_place = forms.CharField(max_length=50)
    amount_of_people = forms.IntegerField(min_value=1)
    date = forms.DateField(widget=forms.SelectDateWidget())
