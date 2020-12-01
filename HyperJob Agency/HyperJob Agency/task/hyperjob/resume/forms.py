from django import forms
from .models import Resume


class NewResume(forms.Form):
    description = forms.CharField()

    class Meta:
        model = Resume
        fields = ('author', 'description')
