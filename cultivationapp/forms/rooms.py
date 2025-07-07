from django import forms
from ..models import PlantRoom

class PlantRoomForm(forms.ModelForm):
    class Meta:
        model = PlantRoom
        fields = [
            'name',
            'width',
            'height',
            'temperature',
            'humidity',
            'light_cycle_hours',
        ]
        labels = {
            'name': 'Nombre de la sala',
            'width': 'Columnas (ancho)',
            'height': 'Filas (alto)',
            'temperature': 'Temperatura (°C)',
            'humidity': 'Humedad (%)',
            'light_cycle_hours': 'Ciclo de luz (horas)',
        }
        help_texts = {
            'width': 'Número de columnas tipo Excel (A, B, C...)',
            'height': 'Número de filas (1, 2, 3...)',
        }

    def clean(self):
        cleaned_data = super().clean()
        width = cleaned_data.get('width')
        height = cleaned_data.get('height')
        capacity = cleaned_data.get('max_capacity')

        if width and height and capacity:
            max_possible = width * height
            if capacity > max_possible:
                self.add_error('max_capacity', f'Capacidad no puede exceder {max_possible} ({width}x{height})')
