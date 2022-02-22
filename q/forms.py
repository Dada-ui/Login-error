from django import forms
from q.models import *

class Register_form(forms.ModelForm):
    class Meta:
        model = Register_model
        fields = '__all__'
        

class Login_form(forms.ModelForm):
    class Meta:
        model = Login_model
        fields = ['username','password']


class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact_model
        fields = '__all__'
