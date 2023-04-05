
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms





class Log(forms.Form):
     username=forms.CharField(max_length=50,label="Username",widget=forms.TextInput(attrs={"placeholder":"Username","class":"form-control"}))
     password1=forms.CharField(max_length=50,label="Password",widget=forms.PasswordInput(attrs={"placeholder":"Password","class":"form-control"}))


class Reg(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']        



        
    