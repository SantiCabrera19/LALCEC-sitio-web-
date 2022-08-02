from django.shortcuts import render
from .models import Libro
# Create your views here.
def listar_todos(request):
    lista = Libro.objects.all().order_by('titulo')
    context = {'lista': lista}
    return render(request, 'listar.html', context)

def filtrar_por_id(request, id):
    libro = Libro.objects.get(id=id)
    context = {'libro': libro}
    return render(request, 'detalle.html', context)
