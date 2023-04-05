from django import forms
from .models import *




class BioForm(forms.ModelForm):
    class Meta:
        model=Bio
        exclude=["user"]
        widgets={
            
            "dob":forms.DateInput(attrs={"class":"form-control","type":"date"}),
            "gender":forms.RadioSelect(attrs={}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            "status":forms.TextInput(attrs={"class":"form-control"}),
            
            
        }
        

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=["image","caption"]
        widget={
            "image":forms.FileInput(),
            "caption":forms.TextInput(attrs={"class":"form-control"}),
            
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=["comment"]
        widgets={
            "comment":forms.TextInput(attrs={"class":"form-control"}),
            
        }

class ChangePassForm(forms.Form):
    # username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"username","class":"form-control"}))
    c_pass=forms.CharField(max_length=50,label="Current Password",widget=forms.PasswordInput(attrs={"placeholder":"Current Password","class":"form-control"}))
    new_pass=forms.CharField(max_length=50,label="New Password",widget=forms.PasswordInput(attrs={"placeholder":"New Password","class":"form-control"}))
    con_pass=forms.CharField(max_length=50,label="Confirm Password",widget=forms.PasswordInput(attrs={"placeholder":"Confirm Password","class":"form-control"}))
       