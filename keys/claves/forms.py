from django import forms 
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item 
        fields=['url', 'username', 'password', 'categoria', 'remarks']
        widgets={
            'url':forms.TextInput(attrs={'class': 'form-control'}),
            'username':forms.TextInput(attrs={'class': 'form-control'}),
            'password':forms.TextInput(attrs={'class': 'form-control'}),
            'categoria':forms.Select(attrs={'class': 'form-control'}),
            'remarks':forms.TextInput(attrs={'class': 'form-control'}),
        }