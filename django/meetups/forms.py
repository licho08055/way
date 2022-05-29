from dataclasses import fields
from django import forms
 


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')
    