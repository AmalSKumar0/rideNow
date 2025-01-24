from django import forms

class PassengerLoginForm(forms.Form):
    email_id = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

class searchAuto(forms.Form):
    from_loc = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Current location", 'id': 'autocomplete', 'required': True}),
        label="From"  # Optional: adding a label
    )
    to_loc = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Select location", 'id': 'autocomplete2', 'required': True}),
        label="To"  # Optional: adding a label
    )
    landmark = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "Enter your landmark", 'id': 'landmark', 'required': True}),
        label="Landmark"  # Optional: adding a label
    )

class PassengerRegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'})
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'})
    )
    
    gender = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    address = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'})
    )
    
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'form-control'})
    )
    
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
    
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'form-control'})
    )
    
    # Clean method to validate passwords match
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")


