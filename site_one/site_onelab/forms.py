from django import forms
from django.core.exceptions import ValidationError
from .models import UserProfile



class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, error_messages={
        'required': 'Обязательное поле'
    })
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput, error_messages={
        'required': 'Обязательное поле'
    })

    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise ValidationError({
                'password2': ValidationError('Введенные пароли не совпадают', code='password_missmatch')
            })

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'email')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
