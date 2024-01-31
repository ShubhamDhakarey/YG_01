# forms.py

from django import forms
from .models import Feedback
from .models import Card

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'site', 'image', 'message']

    # Add any additional form validations as needed

class ImageForm(forms.ModelForm):
    class Meta:
         model = Card
         fields = '__all__'
         labels = {'image':''}