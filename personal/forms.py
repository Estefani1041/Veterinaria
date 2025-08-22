from django import forms
from .models import Personal


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['nombre', 'apellido']  # pon todos los campos que quieras editar
