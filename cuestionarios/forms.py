from django import forms

from .models import Reactivo


class BusquedaFormulario(forms.ModelForm):
	busqueda = forms.CharField(label="Búsqueda", required=True)
	class Meta:
		model = Reactivo
		fields = ['tema']
		widgets = {
        	'tema': forms.Select(
        		attrs={'id': 'id_tema'}
        	),
        }

	def __init__(self, *args, **kwargs):
		super(BusquedaFormulario, self).__init__(*args, **kwargs)
		self.fields['busqueda'].widget = forms.TextInput(attrs={
			'id': 'id_text',
			'placeholder': 'Say something ...'}
		)


class CrearReactivo(forms.ModelForm):
	class Meta:
		model = Reactivo
		fields = ['tema', 'respuesta', 'pregunta']

