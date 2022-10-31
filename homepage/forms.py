from homepage.models import Article_Cashflow
from django.forms import ModelForm, TextInput, HiddenInput

class CreateComment(ModelForm):

    class Meta:
        model = Article_Cashflow
        fields = ('comment_anonymous',)
        widgets = {
            'comment_anonymous': TextInput(attrs={
                    'id':"komentar",
                    'name' :"comment",
                    'class': "form-control",
                    'style': 'max-width: 300px;',
                    'placeholder': 'Name'
                    
                }),
            'comment_anoymous' : HiddenInput(),
            }
