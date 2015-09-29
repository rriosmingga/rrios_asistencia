from django.db import models

class Colegio(models.Model):
	nombre = models.CharField(max_length=150)

class Curso(models.Model):
	colegio = models.ForeignKey(Colegio)
	nivel = models.CharField(max_length=20)
	paralelo = models.CharField(max_length=5)

class Alumno(models.Model):
	rut = models.CharField(max_length=13)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)

class ListaCurso(models.Model):
	periodo = models.CharField(max_length=10)
	alumno = models.ForeignKey(Alumno)
	curso = models.ForeignKey(Curso)

class Asistencia(models.Model):
	lista = models.ForeignKey(ListaCurso)
	fecha = models.DateField()
	estado = models.CharField(max_length=20)

class Profesor(models.Model):
	rut = models.CharField(max_length=13)
	nombres = models.CharField(max_length=100)
	apellidos = models.CharField(max_length=100)

class ProfesorJefe(models.Model):
	periodo = models.CharField(max_length=10)
	profesor = models.ForeignKey(Profesor)
	curso = models.ForeignKey(Curso)