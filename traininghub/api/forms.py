from dataclasses import field
from django import forms
from .models import Training

class TrainingForm(forms.ModelForm):
    
    class Meta:
        model=Training
        fields=('title','description','category','training_link')