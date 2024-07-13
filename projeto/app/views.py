from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.form import UsuarioForm
from app.models import Usuario
from django.contrib.auth import authenticate, login



# funções de autenticação

"""def login(request):
    return render(request, 'login.html')

def dologin(request):
    user = authenticate(username= request.POST['name'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('index.html')
    else:
        return render(request='login.html')
"""

def home(request):
    data = {}
    data['db'] = Usuario.objects.all()
    return render(request,'index.html', data)

def form(request):
    data = {}
    data['form'] = UsuarioForm
    return render(request, 'form.html', data)

def create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def view(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data={}
    data['db'] = Usuario.objects.get(pk=pk)
    data['form'] = UsuarioForm(instance=data['db'])
    return render(request, 'form.html',data)

def update(request, pk):
    data = {}
    data['db'] = Usuario.objects.get(pk=pk)
    form = UsuarioForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(requeste, pk):
    db = Usuario.objects.get(pk=pk)
    db.delete()
    return redirect('home')