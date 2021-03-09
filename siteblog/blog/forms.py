from django import forms
from django.core.mail import send_mail



class DateForm(forms.Form):
    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H'])

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", }))
    message = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'}))
