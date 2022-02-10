from django.shortcuts import redirect, render
import requests

from django import forms

from fr.forms import *
from django.views.decorators.csrf import csrf_protect
# Create your views here.

endpoint = 'http://localhost:5000{}'

def index(request):
    res ={}
    if request.method == 'GET':
        
        url = endpoint.format('/get')
        data = requests.get(url,res)
        res['data'] = data.json
        return render(request,'index.html',res)

    elif request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            json_data = form.cleaned_data
            print(json_data)
            url = endpoint.format('/post')
            response = requests.post(url, json=json_data)
            if response.ok:
                print('response ok')
                return render(request, 'index.html', {'form':form})
        return render(request, 'index.html', {'form':form})

    elif request.method == 'DELETE':
        nopedido = request.form.get('nopedido_')
        if not nopedido :
            res['error'] = 1
            return render(request,'index.html',res)
        res['nopedido_d']
        url = endpoint.format('/post')
        data = requests.get(url,res)
        return redirect('GET','index.html')