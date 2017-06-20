from django import forms

class ProgressForm(forms.Form):
    generations_complete = forms.IntegerField(
            widget=forms.NumberInput(attrs=
                {
                    'class':'form-control',
                    'name':'generations_complete',
                    'size':'50',
                    'min': '0',
                    'max': '10',
                    'default': '0',
                })
    )
