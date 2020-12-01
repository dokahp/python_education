from django import forms
from .models import Vacancy


class NewVacancy(forms.Form):
    description = forms.CharField()

    class Meta:
        model = Vacancy
        fields = ('author', 'description')
