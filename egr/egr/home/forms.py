from django import forms

class NameForm(forms.Form):
    fname = forms.CharField(label='Your First name',max_length=100)
    lname = forms.CharField(label='Your Last name',max_length=100)
