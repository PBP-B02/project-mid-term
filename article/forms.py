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
                'placeholder':"Title"
            }),
            'konten': forms.Textarea(attrs={
                'required': True,
                'name':"konten",
                'id':"konten", 		
                'placeholder':"Content",
            }),
            'author': forms.TextInput(attrs={
                'required': True,
                'name':"author",
                'id':"author",
                'placeholder':"Author"
            }),
        }
