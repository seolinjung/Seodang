from django import forms
from django.core.exceptions import ValidationError
from langdetect import detect

from .models import Input

class InputForm(forms.ModelForm):

    class Meta:
        model = Input
        fields = ('text')