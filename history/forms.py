from django import forms

BUDGET_TYPE= [
    ('income', 'Income'),
    ('spending', 'Spending'),
    ]
  
# creating a form 
class HistoryForm(forms.Form):
    budget_type = forms.ChoiceField(choices = BUDGET_TYPE, label="")