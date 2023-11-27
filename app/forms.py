# a form to handle the button click and any additional information you want to collect.

from django import forms

class OnlineStatusForm(forms.Form):
    set_online = forms.BooleanField(initial=False,required=False, widget=forms.HiddenInput)