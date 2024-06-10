from django import forms 

from album.models import Album


class album_form(forms.ModelForm):
    class Meta:
        model=Album
        fields='__all__'

    labels={
       'date':'Album release date',
       'name':'Album Name'
    }
   