import json

from django.core.serializers import serialize
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import Reactivo, Tema
from .forms import BusquedaFormulario, CrearReactivo

# Create your views here.

class Home(View):
	def get(self, request, *args,**kwargs):
		busqueda_form = BusquedaFormulario()
		preguntas_count = Reactivo.objects.all().count()	
		quizzes_count = Tema.objects.all().count()	
		return render(
			request, 
			"busca_reactivo.html",
				{
					"busqueda_form": busqueda_form,
					"quizzes": quizzes_count-1,
					"preguntas": preguntas_count,
				}
			)

def crear_reactivo(request):
	if request.method == 'POST':
		form_reactivo = CrearReactivo(request.POST)
		if form_reactivo.is_valid():
			form_reactivo.save()
			return redirect('/quizzes/crear_reactivo/')
	else:
		form_reactivo = CrearReactivo()
	return render(
		request, 
		'crea_reactivo.html',
		{
			'form_reactivo': form_reactivo
		}

	)

def editar_reactivo(request, id):
	error=None
	form_reactivo=None
	try:
		reactivo = Reactivo.objects.get(id=id) 
		if request.method == 'GET':
			form_reactivo = CrearReactivo(instance=reactivo)
		else:
			form_reactivo = CrearReactivo(request.POST, instance= reactivo)		
			if form_reactivo.is_valid():
				form_reactivo.save()
				return redirect('home')
	except ObjectDoesNotExist as e:
		error = e
	return render(
		request, 
		'crea_reactivo.html',
		{
			'form_reactivo': form_reactivo,
			'error': error
		}
	)

def eliminar_reactivo(request, id):	
	reactivo = Reactivo.objects.get(id=id) 
	reactivo.delete()
	return redirect('home')

def realizar_busqueda(request):
	if request.method == "GET":
		busqueda = request.GET.get('busqueda')
		id_tema=int(request.GET.get('tema'))
		nombre_tema = Tema.objects.get(id=id_tema).nombre
		if nombre_tema!='Todos':
			reactivos=Reactivo.objects.filter(
				Q(pregunta__icontains=busqueda)|Q(respuesta__icontains=busqueda),
				tema=id_tema
			) 
		else:
			reactivos=Reactivo.objects.filter(
				Q(pregunta__icontains=busqueda)|Q(respuesta__icontains=busqueda)
			)
		data=[]
		for item in reactivos:
			data.append({
					'pregunta': item.pregunta,
					'respuesta': item.respuesta, 
					'id': item.id,
					'tema': item.tema.nombre 
				})				
		return HttpResponse(json.dumps(data), 'application/json')
	else:
		return redirect('home')
