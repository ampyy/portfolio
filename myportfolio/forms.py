from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input-field'
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'input-field'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'input-field'
    }))
    msg = forms.CharField(widget=forms.Textarea(attrs={
        'class' : 'input-field',
    }), label="Your Message")

    class Meta:
        model = Contact
        fields = ('name', 'subject', 'email', 'msg')