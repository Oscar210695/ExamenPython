from django.shortcuts import render, HttpResponse, redirect
import requests
from django.contrib import messages
from ilusionesMain.forms import FormAlmacen, EditFormAlmacen
from ilusionesAPI.models import Almacen

# Create your views here.
def index(request):
    return render(request, 'index.html', {
            'title': 'Inicio'
        })

def getAlmacenes(request):
    resp = requests.get('http://127.0.0.1:8000/api/posts/')

    almacenes = []

    if resp.status_code != 200:
        return HttpResponse(f"<h2>Se ha generado un error al consultar la API</h2")
    for almacen in resp.json():
        almacenes.append({
            'subInventario': almacen['subInventario'],
            'pdv': almacen['pdv'],
            'nombre': almacen['nombre'],
        })

    return render(request, 'almacen/almacenes.html',{
        'title': 'Almacenes',
        'almacenes': almacenes
    })

def deleteAlmacen(request, subInventario):
    resp = requests.delete('http://127.0.0.1:8000/api/posts/'+subInventario)

    if resp.status_code != 200 and resp.status_code != 204:
         messages.success(request, f'No se ha podido borrar el registro')
    else:
        messages.success(request, f'Se borro correctamente el almacen')
    
    return redirect('almacenes')

def getAlmacen(request, subInventario):
    resp = requests.get('http://127.0.0.1:8000/api/posts/'+subInventario)

    if resp.status_code != 200:
            messages.success(request, f'No se ha podido encontrar la información')
            return redirect('almacenes')

    if request.method == 'POST':
        almacen = Almacen(pdv=resp.json()['pdv'],nombre=resp.json()['nombre'])

        formulario = EditFormAlmacen(request.POST, instance=almacen)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            subInventario = subInventario
            pdv = data_form['pdv']
            nombre = data_form['nombre']

            resp = requests.put('http://127.0.0.1:8000/api/posts/'+subInventario+'/', json={'subInventario':subInventario,'pdv':pdv,'nombre':nombre})

            if resp.status_code != 200:
                messages.success(request, f'No se ha podido actualizar el Almacen {subInventario}')
                return redirect('almacenes')

            #mensaje Flask
            messages.success(request, f'Se ha actualizado correctamente el inventario {subInventario}')

            return redirect('almacenes')
    else:
        formulario = FormAlmacen(
            initial={'subInventario':resp.json()['subInventario'], 
                    'pdv':resp.json()['pdv'],
                    'nombre':resp.json()['nombre']}
        )

        formulario.fields['subInventario'].widget.attrs['readonly'] = True

    return render(request, 'almacen/alterAlmacen.html', {
        'title': f'Actualizar almacen <i>{subInventario}</i>',
        'form': formulario,
        'button': 'Actualizar'
    })

def deleteAlmacen(request, subInventario):
    resp = requests.delete('http://127.0.0.1:8000/api/posts/'+subInventario)

    if resp.status_code != 200 and resp.status_code != 204:
         messages.success(request, f'No se ha podido borrar el registro')
    else:
        messages.success(request, f'Se borro correctamente el almacen')
    
    return redirect('almacenes')

def saveAlmacen(request):
    if request.method == 'POST':
        formulario = FormAlmacen(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            subInventario = data_form.get('subInventario')
            pdv = data_form['pdv']
            nombre = data_form['nombre']

            resp = requests.post('http://127.0.0.1:8000/api/posts/', json={'subInventario':subInventario,'pdv':pdv,'nombre':nombre})

            if resp.status_code != 201:
                messages.success(request, f'No se ha podido guardar el Almacen {subInventario}')
                return redirect('almacenes')

            #mensaje Flask
            messages.success(request, f'Se ha guardado correctamente el inventario {subInventario}')

            return redirect('almacenes')
    else:
        formulario = FormAlmacen()

    return render(request, 'almacen/alterAlmacen.html', {
        'title': f'Crear Almacen',
        'form': formulario,
        'button': 'Guardar'
    })

