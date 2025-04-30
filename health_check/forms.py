from django import forms
from .models import DeliveringValue

class DeliveringValueForm(forms.ModelForm):
    class Meta:
        model = DeliveringValue
        fields = ['color_status', 'reason', 'improvement']
