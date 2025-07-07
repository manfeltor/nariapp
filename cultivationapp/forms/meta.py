# cultivationapp/forms/meta.py
from django import forms
from cultivationapp.models.meta import Sex, Species, Breed, PlantStatus, PlantPhase

class SexForm(forms.ModelForm):
    class Meta:
        model = Sex
        fields = ['name', 'abbreviation', 'description']
        labels = {
            'name': 'Nombre',
            'abbreviation': 'Abreviatura',
            'description': 'Descripción',
        }

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre Científico o Común',
            'description': 'Descripción',
        }

class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['species', 'name', 'description']
        labels = {
            'species': 'Especie',
            'name': 'Nombre de la Variedad',
            'description': 'Descripción',
        }

class PlantStatusForm(forms.ModelForm):
    class Meta:
        model = PlantStatus
        fields = ['name', 'description', 'phase_group']
        labels = {
            'name': 'Estado',
            'description': 'Descripción',
            'phase_group': 'Grupo de Fase',
        }

class PlantPhaseForm(forms.ModelForm):
    class Meta:
        model = PlantPhase
        fields = ['name', 'description']
        labels = {
            'name': 'Nombre de Fase',
            'description': 'Descripción',
        }
