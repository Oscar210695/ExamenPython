from django.shortcuts import render, HttpResponse, redirect
import requests
from django.contrib import messages
from ilusionesMain.forms import FormAlmacen, EditFormAlmacen, FormOrden, FormRec
from ilusionesAPI.models import Almacen
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'index.html', {
            'title': 'Inicio'
        })

def getAlmacenes(request):
    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/almacen/'

    resp = requests.get(ruta)

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
    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/almacen/' + subInventario + '/'
    resp = requests.delete(ruta)

    if resp.status_code != 200 and resp.status_code != 204:
         messages.success(request, f'No se ha podido borrar el registro')
    else:
        messages.success(request, f'Se borro correctamente el almacen')
    
    return redirect('almacenes')

def getAlmacen(request, subInventario):
    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/almacen/' + subInventario + '/'
    resp = requests.get(ruta)

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

            resp = requests.put(ruta, json={'subInventario':subInventario,'pdv':pdv,'nombre':nombre})

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

def saveAlmacen(request):
    if request.method == 'POST':
        formulario = FormAlmacen(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            subInventario = data_form.get('subInventario')
            pdv = data_form['pdv']
            nombre = data_form['nombre']

            ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/almacen/'
            resp = requests.post(ruta, json={'subInventario':subInventario,'pdv':pdv,'nombre':nombre})

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

def loadCompras(request):
    if request.method == 'POST':
        formulario = FormOrden(request.POST, request.FILES)
        
        if formulario.is_valid():
            data_form = formulario.cleaned_data

            orden = data_form.get('clave')

            df = pd.read_excel(request.FILES.get('Archivo'), index_col=0)
            df = df.sort_index()
            df = df[:-1]
            non_null_columns = [col for col in df.columns if df.loc[:, col].notna().any()]
            df = df[non_null_columns]

            if df.index.name == 'Sub inventario' and df.columns[0] == 'PDV' and df.columns[-1] == 'TOTAL':
                df = df.loc[df['TOTAL'] > 0]
                df = df.drop(columns="TOTAL")

                repetidos = df.index.get_level_values('Sub inventario').get_duplicates()

                if len(repetidos) > 0:
                    messages.success(request, f'El archivo contiene inventarios duplicados')
                else:
                    almacenes = list(df.index.values)
                    for almacen in almacenes:
                        ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/almacen/' + almacen + '/'
                        resp = requests.get(ruta)

                        if resp.status_code != 200:
                                messages.success(request, f'No se encuentran todos los almacenes regitrados')
                                return redirect('subirOrden')

                    productos = list(df.columns[1:])
                    
                    for producto in productos:
                        producto = producto.replace(".", "_")

                        ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/prod/' + producto + '/'
                        resp = requests.get(ruta)

                        if resp.status_code != 200:
                                ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/prod/'
                                resp = requests.post(ruta, json={'sku':producto})

                                if resp.status_code != 201:
                                    messages.success(request, f'No se ha podido guardar el producto {producto}')
                                    return redirect('subirOrden')

                    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/ordenIn/'
                    resp = requests.post(ruta, json={'clave':orden,'total':0, 'entregada':False})

                    if resp.status_code != 201:
                        messages.success(request, f'No se ha podido guardar la orden principal')
                        return redirect('subirOrden')

                    df = df.fillna(0).drop(columns="PDV")
                    suma=0
                    for i, j in df.iterrows(): 
                        almacen = i
                        for column in df.columns:
                            producto = column.replace('.','_')
                            cantidad = df[column][i]
                            if cantidad > 0:
                                estatus = 1
                                suma += cantidad

                                ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/orden/'
                                resp = requests.post(ruta, json={'almacen':almacen,'producto':producto,'cantidad':cantidad, 'estatus': estatus, 'orden': orden})

                                if resp.status_code != 201:
                                    messages.success(request, f'No se ha podido guardar la orden')
                                    return redirect('subirOrden')

                    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/ordenIn/' + orden + '/'

                    resp = requests.put(ruta, json={'clave':orden,'total':suma, 'entregada':False})

                    if resp.status_code != 200:
                        messages.success(request, f'No se ha podido actualizar la orden {orden}')
                        return redirect('subirOrden')

                    messages.success(request, f'Se agregraron correctamente las ordenes de compra')
                    return redirect('ordenes')

            else:
                messages.success(request, f'El archivo no contiene el formato adecuado')
    else:
        formulario = FormOrden()

    return render(request, 'compras/loadCompras.html', {
        'title': f'Cargar Orden de Compra',
        'form': formulario,
    })

def getOrdenes(request):
    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/ordenIn/'

    resp = requests.get(ruta)

    ordenes = []

    if resp.status_code != 200:
        return HttpResponse(f"<h2>Se ha generado un error al consultar la API</h2")
    for orden in resp.json():        
        ordenes.append({
            'clave': orden['clave'],
            'total': orden['total'],
            'entregada': orden['entregada']
        })

    formulario = FormRec()
        
    return render(request, 'compras/ordenes.html',{
        'title': 'Ordenes generadas',
        'ordenes': ordenes,
        'form': formulario
    })

def loadRec(request, orden):
    if request.method == 'POST':
        formulario = FormRec(request.POST, request.FILES)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            df = pd.read_excel(request.FILES.get('Archivo_Recepcion'), index_col=0)

            if df.index.name == 'SUBINVENTARIO' and df.columns[0] == 'NOMBRE' and df.columns[1] == 'MODELO' and df.columns[2] == 'IMEI' and df.columns[3] == 'FOLIO':

                almacenes = list(df.index.unique())
                for almacen in almacenes:
                    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/almacen/' + almacen + '/'
                    resp = requests.get(ruta)

                    if resp.status_code != 200:
                            messages.success(request, f'No se encuentran todos los almacenes regitrados')
                            return redirect('ordenes')

                repetidos = df[df.duplicated(['IMEI'])]

                if len(repetidos) > 0:
                     messages.success(request, f'El archivo contiene IMES´s duplicados')
                else:
                    dfRec = df[['NOMBRE','FOLIO']].reset_index().drop_duplicates(subset=['SUBINVENTARIO','NOMBRE','FOLIO'])
                    dfProd = df[['FOLIO','MODELO','IMEI']].reset_index()

                    for x,y in dfRec.iterrows(): 
                        almacen = y['SUBINVENTARIO']
                        nombre = y['NOMBRE']
                        folio = y['FOLIO']

                        ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/recep/'
                        resp = requests.post(ruta, json={'almacen':almacen,'nombre':nombre,'folio':folio, 'orden':orden})

                        if resp.status_code != 201:
                            messages.success(request, f'No se ha podido guardar el registro de recepción debido a ya existen folios dados de alta')
                            return redirect('ordenes')
                    
                    modelos = dfProd[['MODELO']].drop_duplicates(subset=['MODELO'])
                    for x,y in modelos.iterrows(): 
                        producto = y['MODELO'].replace('.','_')

                        ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/prod/' + producto + '/'
                        resp = requests.get(ruta)

                        if resp.status_code != 200:
                                ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/prod/'
                                resp = requests.post(ruta, json={'sku':producto})

                                if resp.status_code != 201:
                                    messages.success(request, f'No se ha podido guardar el producto {producto}')
                                    return redirect('ordenes')

                    for x,y in dfProd.iterrows(): 
                        imei = y['IMEI']
                        producto = y['MODELO'].replace('.','_')
                        folio = y['FOLIO']

                        ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/inven/'
                        resp = requests.post(ruta, json={'imei':imei,'producto':producto,'folio':folio})

                        if resp.status_code != 201:
                            messages.success(request, f'No se ha podido guardar el registro del producto, puede que este ya exista alguno con el mismo IMEI')
                            return redirect('ordenes')

                    ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/ordenIn/' + orden + '/'

                    resp = requests.put(ruta, json={'clave':orden, 'entregada':True})

                    if resp.status_code != 200:
                        messages.success(request, f'No se ha podido actualizar la orden {orden}')
                        return redirect('ordenes')
                    
                    messages.success(request, f'Se ha cargado correctamente el archivo')
            else:
                messages.success(request, f'El archivo no contiene el formato adecuado')

        else:
            ruta = 'http://' + request.META.get('HTTP_HOST') + '/api/ordenIn/'

            resp = requests.get(ruta)

            ordenes = []

            if resp.status_code != 200:
                return HttpResponse(f"<h2>Se ha generado un error al consultar la API</h2")
            for orden in resp.json():        
                ordenes.append({
                    'clave': orden['clave'],
                    'total': orden['total'],
                    'recep': orden['recep']
                })

            return render(request, 'compras/ordenes.html',{
                'title': 'Ordenes generadas',
                'ordenes': ordenes,
                'form': formulario
            })

    return redirect('ordenes')
