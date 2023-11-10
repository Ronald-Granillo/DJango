from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from models import alumnos
from django.views.decorators.csrf import csrf_exempt

def saludo(request):
    return HttpResponse("Hola desde django")

def miEdad(request, edad):
    return HttpResponse("Hola tu edad es: %s" %edad)

def index(request):
    return render(request, 'index.html')


def alumno(request):
    return render(request, 'alumnos.html')

def buscar(request):
    return render(request, 'busqueda_alumnos.html')

@csrf_exempt
def buscar_alumno(request):
    data = json.loads(request.body)
    datos = alumnos.objects.filtrer(nombre_iconstains=data.get('buscar')).values('id','codigo','nombre','direccion','telefono')
    return JsonResponse(list(datos), safe=False)
def materia(request):
    return render(request, 'materia.html')

def buscarM(request):
    return render(request, 'busqueda_materia.html')

def docente(request):
    return render(request, 'docente.html')
 