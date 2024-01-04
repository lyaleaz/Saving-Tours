from django import forms
from .models import Driver

class MyfileuploadForm(forms.Form):
    filename=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
class contactformemail(forms.Form):
    frommail=forms.EmailField(required=True)
    subject=forms.CharField(required=True)
    message=forms.CharField(required=True)
