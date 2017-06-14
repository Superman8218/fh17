from django import forms

class ProgressForm(forms.Form):
    generation_complete = forms.IntegerField()

