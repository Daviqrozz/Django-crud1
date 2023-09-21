from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Pessoa

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error_message = "Nome ou senha incorretos!"
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def home(request):
    pessoas = Pessoa.objects.all()
    return render(request,"index.html",{'pessoas':pessoas})

def cadastro(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro.html',{'pessoas':pessoas})

def salvar(request):
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")

    Pessoa.objects.create(nome=nome, idade=idade)
    pessoas = Pessoa.objects.all()

    return render(request, 'index.html', {'pessoas': pessoas})

def editar(request,id):
    pessoa = Pessoa.objects.get(id=id)
    return render(request,'update.html',{'pessoa':pessoa})

def update(request,id):
    nome = request.POST.get("nome")
    idade = request.POST.get("idade")
    pessoa = Pessoa.objects.get(id=id)
    pessoa.nome = nome
    pessoa.idade = idade
    pessoa.save()
    return redirect(home)

def delete(request,id):
    pessoa = Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect(home)