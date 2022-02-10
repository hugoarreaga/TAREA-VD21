from django.shortcuts import render, redirect
import requests

# Create your views here.
endpoint = 'http://localhost:5000{}'

def index(request):
    if request.method == 'GET':
        url = endpoint.format('/login')
        usuario = request.GET.get('usuario')
        password = request.GET.get('contrasena')
        res ={}
        if not usuario or not password:
            res['mensaje'] = 'Debe de llenar todos los campos'
            return render(request,'index.html',res)

        name_usuario = requests.get(url, {
            'usuario': usuario,
            'contrasena': password,
        })
        
        res['usuario'] = name_usuario.text

        if name_usuario.text =='None':
            res['mensaje'] = 'Usuario no existe'
            return render(request,'index.html',res)

        return render(request,'inicio.html',res)
    
def inicio(request):
    return render(request,'inicio.html')