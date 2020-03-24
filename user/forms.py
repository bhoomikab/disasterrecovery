from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from user.models import User, Administrator


class AdminSignupForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Required')

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('username', 'first_name', 'last_name', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_admin = True
        if commit:
            user.save()
        return user


class ContractorSignupForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=True, help_text='Required')
    # last_name = forms.CharField(max_length=30, required=True, help_text='Required')

    class Meta(UserCreationForm.Meta):
        model = User
        # fields = ('username', 'first_name', 'last_name', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_contractor = True
        if commit:
            user.save()
        return user
