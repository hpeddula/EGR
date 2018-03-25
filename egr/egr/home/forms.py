from django import forms

class NameForm(forms.Form):
    fname = form.CharField(label='Your First name',max_length=100)
    lname = form.CharField(label='Your Last name',max_length=100)
