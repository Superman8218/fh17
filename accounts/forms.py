from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserFormMixin(forms.Form):

    username = forms.CharField(
            label='Username',
            widget=forms.TextInput(attrs=
                {
                    'class':'form-control',
                    'name':'username',
                    'placeholder':'User Name',
                    'size':'50'
                })
            )

    password1 = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(attrs=
                {
                    'class':'form-control',
                    'name':'password1',
                    'placeholder':'Password',
                    'size':'50'
                })
            )

    password2 = forms.CharField(
            label='Password (again)',
            widget=forms.PasswordInput(attrs=
                {
                    'class':'form-control',
                    'name':'password2',
                    'placeholder':'Password (again)',
                    'size':'50'
                })
            )

class RegistrationForm(UserFormMixin, UserCreationForm): 
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.order_fields(['username', 'password1', 'password2'])
