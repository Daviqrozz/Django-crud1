from django.shortcuts import render,redirect
from .models import Pessoa

def home(request):
    pessoas = Pessoa.objects.all()
    return render(request,"index.html",{'pessoas':pessoas})


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