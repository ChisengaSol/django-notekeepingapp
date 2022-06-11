from django import forms
from .models import Note,Languangedetails
from django.contrib.auth.models import User


class NoteCreationForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','languange_name','description']

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','languange_name','description']

class AccountSettingsForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name']

class CreateProgrammingLangForm(forms.ModelForm):
    class Meta:
        model = Languangedetails
        fields = ['languange_name','is_language']