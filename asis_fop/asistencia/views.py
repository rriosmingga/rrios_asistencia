from django.http import HttpResponse


def index(request):
    return HttpResponse("Funcionando app de asistencia")