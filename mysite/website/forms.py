from django import forms
from .models import Member

class Memberform(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname','lname','email','age','passwd']
