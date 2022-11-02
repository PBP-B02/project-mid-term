
from django import  forms

class NameArticle(forms.Form):
    article = forms.CharField(label="",max_length = 100, required=False)