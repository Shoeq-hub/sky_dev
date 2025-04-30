from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreateForm(UserCreationForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in self.fields:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})
            self.fields[fieldname].help_text = None

