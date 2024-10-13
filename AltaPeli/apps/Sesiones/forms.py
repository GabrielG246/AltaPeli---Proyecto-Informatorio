from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Agregar el campo de email
    lastname = forms.CharField(max_length=150, required=True)  # Agregar el campo de apellido

    class Meta:
        model = User
        fields = ('username', 'lastname', 'email', 'password1', 'password2')  # Asegúrate de incluir los campos que deseas

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.last_name = self.cleaned_data['lastname']  # Establecer el apellido
        if commit:
            user.save()
        return user
