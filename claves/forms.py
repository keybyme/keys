from django import forms 
from .models import Item, Contacto, Qrcode

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

class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto 
        fields=['name', 'address', 'phone', 'email', 'catpeople']
        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class': 'form-control'}),
            'phone':forms.TextInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'catpeople':forms.Select(attrs={'class': 'form-control'}),
        }    


class QrcodeForm(forms.ModelForm):
    class Meta:
        model=Qrcode
        fields=["link"]
        widgets={
            'link':forms.ClearableFileInput(attrs={'class': 'form-control'})
        }            

class QrcodeForm2(forms.Form):
    link = forms.URLField(label='Link')        