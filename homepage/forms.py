from django.forms import forms
from homepage.models import Article_Cashflow
from django.forms import ModelForm

class CreateComment(ModelForm):

    class Meta:
        model = Article_Cashflow
        fields = ('user', 'date','comment_anonymous')
