from django import forms
from django.core.exceptions import ValidationError
from langdetect import detect
from django.forms import ModelForm

from .models import Input

class InputForm(ModelForm):

    class Meta:
        model = Input
        fields = ['text']
        labels = { 'text': '', }

    # override og clean method
    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get("text")
        
        # if input sentence is not hangul
        detect_result = detect(text)
        if (detect_result != 'ko'):
            raise ValidationError("The given input is not Korean.")
        
        return cleaned_data