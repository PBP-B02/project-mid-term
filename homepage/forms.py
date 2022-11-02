
import imp
from django import  forms
from homepage.models import Bookmark

class NameArticle(forms.Form):
    article = forms.CharField(label="",max_length = 100, required=False)



