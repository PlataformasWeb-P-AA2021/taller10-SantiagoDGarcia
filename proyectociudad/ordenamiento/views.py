from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

from ordenamiento.models import *
from ordenamiento.forms import *

def index(request):
      return render(request, 'index.html')

def ir_parroquias(request):
      parroquias = Parroquia.objects.all()
      return render(request, 'parroquias.html', {'dic': parroquias})

def crear_parroquias(request):
      if request.method=='POST':
            formulario = FormParroquia(request.POST)
            if formulario.is_valid(): 
                  formulario.save()
                  return redirect(ir_parroquias)
      else:
            return render(request, 'crear-parroquia.html',  {'form': FormParroquia}) 
      
def editar_parroquia(request, id ):
      parroquia = Parroquia.objects.get(pk=id)
      if request.method=='POST':
            formulario = FormParroquia(request.POST, instance=parroquia)
            print(formulario.errors)
            if formulario.is_valid():
                  formulario.save()
                  return redirect(ir_parroquias)
      else:
            diccionario = {'form': FormParroquia(instance=parroquia)}
            return render(request, 'editar-parroquia.html', diccionario) 

def ir_barrios_parroquias(request):
      parroquias = Parroquia.objects.all()
      return render(request, 'barrios-parroquias.html', {'dic': parroquias})

      
def crear_barrios(request):
      if request.method=='POST':
            formulario = FormBarrios(request.POST)
            print(formulario.errors)
            if formulario.is_valid(): 
                  formulario.save()
                  return redirect(ir_barrios_parroquias)            
      else:
            return render(request, 'crear-parroquia.html',  {'form': FormBarrios}) 
      
def editar_barrio(request, id ):
      barrio = BarrioCiudadela.objects.get(pk=id)
      if request.method=='POST':
            formulario = FormBarrios(request.POST, instance=barrio)
            print(formulario.errors)
            if formulario.is_valid():
                  formulario.save()
                  return redirect(ir_barrios_parroquias)
      else:
            diccionario = {'form': FormBarrios(instance=barrio)}
            return render(request, 'editar-parroquia.html', diccionario) 
      
def crear_barrio_de_parroquia(request, id):
      parroquia = Parroquia.objects.get(pk=id)
      if request.method=='POST':
            formulario = FormBarrioDeParroquia(parroquia, request.POST)
            print(formulario.errors)
            if formulario.is_valid(): 
                  formulario.save()
                  return redirect(ir_barrios_parroquias)            
      else:
            formulario = FormBarrioDeParroquia(parroquia)
            diccionario = {'form': formulario, 'parroquia': parroquia}
            return render(request, 'crear-barrio-de-parroquia.html', diccionario )