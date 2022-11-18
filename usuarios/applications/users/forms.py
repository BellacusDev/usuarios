from django import forms
#
from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repetir contraseña'
            }
        )
    )

    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )


