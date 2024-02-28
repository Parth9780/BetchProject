from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class updateForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields=['Firstname','Lasttname','Password','username','city','state','mobile']
        
class notesForm(forms.ModelForm):
    class Meta:
        model=user_notes
        fields='__all__'