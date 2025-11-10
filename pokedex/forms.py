from django import forms
from .models import Pokemon
from .models import Trainer

class PokemonForm(forms.ModelForm):
    class Meta:
        model= Pokemon
        fields='__all__'
        labels={
            'name': 'Nombre',
            'type': 'Tipo',
            'weight': 'Peso (kg)',
            'height': 'Altura (cm)',
            'trainer': 'Entrenador',
            'picture': 'Imagen'
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'weight': forms.NumberInput(attrs={'class':'form-control'}),
            'height': forms.NumberInput(attrs={'class':'form-control'}),
            'trainer': forms.Select(attrs={'class':'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class':'form-control'})

        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model= Trainer
        fields='__all__'
        labels={
            'name': 'Nombre',
            'lastname': 'Apellido',
            'birthdate': 'Fecha de Nacimiento',
            'level': 'Nivel',
            'picture': 'Imagen'
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'birthdate': forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'level': forms.NumberInput(attrs={'class':'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class':'form-control'})
        }