from django.shortcuts import render,redirect
from firstApp.forms import FormEquipo
from firstApp.models import Equipo 

 
# Create your views here.

def index(request):
    return render(request,'firstApp/index.html')

def listadoEquipo(request):
    equipos = Equipo.objects.all()
    data = {'equipos':equipos}
    return render(request,'firstApp/equipos.html',data)


def agregarEquipo(request):
    form = FormEquipo()
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'firstApp/agregarEquipo.html', data)
    
def eliminarEquipo(request , id):
    equipo = Equipo.objects.get(id = id)
    equipo.delete()
    return redirect('/equipos',)

def actualizarEquipo(request, id):
    equipo = Equipo.objects.get(id = id)
    form = FormEquipo(instance=equipo)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'firstApp/agregarEquipo.html', data)   
