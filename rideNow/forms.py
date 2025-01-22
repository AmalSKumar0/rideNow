from django import forms
from driver.models import NewDrivers

# class DriverRegistrationForm(forms.ModelForm):
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Enter your password',
#             'id': 'Password'
#         }),
#         label="Password",
#         required=True
#     )
#     confirm_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={
#             'class': 'form-control',
#             'placeholder': 'Confirm your password',
#             'id': 'CPassword'
#         }),
#         label="Confirm Password",
#         required=True
#     )
#     VEHICLE_CHOICES = [
#         ("Auto Rickshaw", "Auto Rickshaw"),
#         ("Economy Car", "Economy Car"),
#         ("Sedan", "Sedan"),
#         ("Luxury Car", "Luxury Car"),
#     ]
#     vehicle_type = forms.ChoiceField(
#         choices=VEHICLE_CHOICES,
#         widget=forms.RadioSelect(attrs={'class': 'form-check-input'})
#     )

#     class Meta:
#         model = NewDrivers
#         fields = [
#             'name', 'email', 'phone', 'address', 
#             'vehicle_type', 'manufacture_date', 
#             'license_number', 'vehicle_number', 'vehicle_image'
#         ]
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your name',
#                 'id': 'name'
#             }),
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your email',
#                 'id': 'email'
#             }),
#             'phone': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your phone number',
#                 'id': 'phone'
#             }),
#             'address': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your address',
#                 'id': 'Address'
#             }),
#             'manufacture_date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'type': 'date',
#                 'id': 'date'
#             }),
#             'license_number': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your license number',
#                 'id': 'License'
#             }),
#             'vehicle_number': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your vehicle number',
#                 'id': 'Vehicle'
#             }),
#             'vehicle_image': forms.FileInput(attrs={
#                 'class': 'form-control-file',
#                 'id': 'image'
#             }),
#         }

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise forms.ValidationError("Passwords do not match.")
