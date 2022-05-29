from django import forms

from .models import Active


class ActiveForm(forms.ModelForm):
    class Meta:
        model = Active
        fields = (
            'bone',
            'name',
            'price',
        )