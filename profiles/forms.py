from django.forms import ModelForm

from models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'group')
