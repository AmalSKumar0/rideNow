from django import forms

class DriverLocForm(forms.Form):
    location = forms.CharField(
        widget=forms.TextInput(attrs={
            'name': 'cloc',
            'id': 'autocomplete',
            'placeholder': 'Current location',
            'required': True
        })
    )
