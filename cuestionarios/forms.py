from django import forms

from .models import Reactivo


class BusquedaFormulario(forms.ModelForm):
	busqueda = forms.CharField(label="Búsqueda", required=True)
	class Meta:
		model = Reactivo
		fields = ['tema']
		widgets = {
        	'tema': forms.Select(
        		attrs={
        			'id': 'id_tema',
        			'class': 'form-control'}
        	),
        }

	def __init__(self, *args, **kwargs):
		super(BusquedaFormulario, self).__init__(*args, **kwargs)
		self.fields['busqueda'].widget = forms.TextInput(attrs={
			'id': 'id_text',
			'placeholder': 'escribe algo ...',
			'class': 'form-control'}
		)


class CrearReactivo(forms.ModelForm):
	class Meta:
		model = Reactivo
		fields = ['tema', 'pregunta', 'respuesta']
		widgets = {
			'tema': forms.Select(
        		attrs={
        			'id': 'id_tema',
        			'class': 'form-control'}), 
      'respuesta': forms.Textarea(
        		attrs={
        			'id': 'id_tema',
        			'class': 'form-control',
        			'rows': "4"}), 

      'pregunta': forms.Textarea(
        		attrs={
        			'id': 'id_tema',
        			'class': 'form-control',
        			'rows': "4"})
		}
