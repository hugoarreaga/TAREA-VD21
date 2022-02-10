from django.shortcuts import render,redirect
import requests


# Create your views here.


endpoint = 'http://localhost:5000{}'    # para realizar la peticion al back


def index(request):
    res={}
    return render(request,'index.html',res)