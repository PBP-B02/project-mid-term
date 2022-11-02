from django import forms

MONTH_CHOICES =(
    ("0", "January"),
    ("1", "February"),
    ("2", "March"),
    ("3", "April"),
    ("4", "May"),
    ("5", "June"),
    ("6", "July"),
    ("7", "August"),
    ("8", "September"),
    ("9", "October"),
    ("10", "November"),
    ("11", "December"),
)

BUDGET_TYPE= [
    ('income', 'Income'),
    ('spending', 'Spending'),
    ]
  
# creating a form 
class HistoryForm(forms.Form):
    # budget_type= forms.CharField(widget=forms.RadioSelect(choices=BUDGET_TYPE))
    budget_type = forms.ChoiceField(choices = BUDGET_TYPE, label="")
    # month_field = forms.ChoiceField(choices = MONTH_CHOICES, label="Choose the month:")