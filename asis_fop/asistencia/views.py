from django.shortcuts import render

from .models import *


def index(request):
	context = Colegio.objects.all()
	return render(request, 'asistencia/index.html', {'lista': context, 'tipo':'colegios'})

def cursos(request, colegio_id):
	colegio = Colegio.objects.get(pk=colegio_id)
	context = Curso.objects.filter(colegio=colegio)
	return render(request, 'asistencia/index.html', {'lista': context, 'tipo':'cursos'})

def lista(request, curso_id, periodo):
	curso = Curso.objects.get(pk=curso_id)
	listacurso = ListaCurso.objects.filter(curso=curso, periodo=periodo)
	context = Alumno.objects.filter(listacurso=listacurso)
	return render(request, 'asistencia/index.html', {'lista': context, 'tipo':'alumnos', 'periodo':periodo, 'curso_id':curso_id})

def pasarlista(request, curso_id, periodo):
	curso = Curso.objects.get(pk=curso_id)
	listacurso = ListaCurso.objects.filter(curso=curso, periodo=periodo)
	context = Alumno.objects.filter(listacurso=listacurso)
	return render(request, 'asistencia/pasarlista.html', {'lista': context})