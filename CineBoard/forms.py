from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm


class CustomRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=13, required=True)
    birth_date = forms.DateField(required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)

    class Meta:
        model = models.CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'birth_date',
        )

        def save(self, commit=True):
            user = super(CustomRegisterForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class FilmForm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields = "__all__"