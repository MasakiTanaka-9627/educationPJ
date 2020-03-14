from django import forms
from .models import BoardImage

class BoardImageForm(forms.ModelForm):
    class Meta:
        model = BoardImage
        fields = ['picture']