from django import forms
from .models import UserTB

# Create your Models Form here.

class User(forms.ModelForm):
    class Meta:
        model = UserTB
        fields = '__all__'
        labels = {
            'name':'Enter You Name',
            'email':'Enter Your Email',
            'password':'Enter Your Password'
            }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={"class":'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
            }