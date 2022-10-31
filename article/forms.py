from django import forms
from article.models import Artikel


class FormArtikel(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ["judul","konten"]   
        widgets = {
            'judul': forms.TextInput(attrs={
                'required': True,
                'name':"judul",
                'id':"judul",
                'style':"background-color: #c3c7bd",
                'placeholder':"Title"
            }),
            'konten': forms.Textarea(attrs={
                'required': True,
                'name':"konten",
                'id':"konten", 
                'style':"background-color: #c3c7bd",		
                'placeholder':"Content",
            }),
        }
