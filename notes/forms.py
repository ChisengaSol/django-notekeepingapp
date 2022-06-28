from django import forms
from .models import Note,Languangedetails
from django.contrib.auth.models import User
from searchableselect.widgets import SearchableSelect

class NoteCreationForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','languange_name','description']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['languange_name'].queryset = Languangedetails.objects.none()
        self.fields['languange_name'].widget.attrs.update({'class' : 'languange_nameclass'})

        if 'languange_name' in self.data:
            self.fields['languange_name'].queryset = Languangedetails.objects.all()

        # elif self.instance.pk:
        #     self.fields['languange_name'].queryset = Languangedetails.objects.all().filter(pk=self.instance.languange_name.pk)

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