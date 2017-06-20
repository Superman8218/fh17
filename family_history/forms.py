from django import forms

class ProgressForm(forms.Form):
    generations = forms.IntegerField(
            widget=forms.NumberInput(attrs=
                {
                    'class':'form-control',
                    'name':'indexed',
                    'size':'50',
                    'min': '0',
                    'max': '10',
                }),
            label='Generations Completed',
            help_text='The total number of generations you have completed so far'

    )

    indexed = forms.IntegerField(
            widget=forms.NumberInput(attrs=
                {
                    'class':'form-control',
                    'name':'indexed',
                    'size':'50',
                    'min': '0',
                    'max': '10',
                }),
            label='Records Indexed',
            help_text='The number of new records you have indexed'

    )

    memories = forms.IntegerField(
            widget=forms.NumberInput(attrs=
                {
                    'class':'form-control',
                    'name':'memories',
                    'size':'50',
                    'min': '0',
                    'max': '10',
                }),
            label='Memories Added',
            help_text='The number of new memories you have added'

    )

    names = forms.IntegerField(
            widget=forms.NumberInput(attrs=
                {
                    'class':'form-control',
                    'name':'names',
                    'size':'50',
                    'min': '0',
                    'max': '10',
                }),
            label='Names',
            help_text='The number of new baptism-elegible names you have found'

    )
