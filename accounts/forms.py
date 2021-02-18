from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import Account
# from phonenumber_field.formfields import PhoneNumberField


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')
    phone_number = forms.IntegerField(
                                        help_text='Required. Add a valid phone number',
                                        validators=[
                                        MinValueValidator(1000000000),
                                        MaxValueValidator(9999999999)
                                        ])

    class Meta:
        model = Account
        fields = ('email','username','phone_number' ,'password1', 'password2', )


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")


class NumberForm(forms.Form):
    number = forms.IntegerField(required=True,help_text="Enter the otp which send to your number")

