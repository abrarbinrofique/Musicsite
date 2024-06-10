from django import forms 

from album.models import Musician


class musician_form(forms.ModelForm):
    class Meta:
        model=Musician
        fields='__all__'

        labels={
             'Firstname': 'First Name',
             'Lastname' : 'Last Name ',
             'Phonenumber':'Phone Number'
         }