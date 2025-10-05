from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Tarefas
# Create your views here.

def adicionar(request):
    if request.method == "POST":
        tarefa = request.POST.get("tarefa")
        tarefas = Tarefas.objects.create(
            tarefa = tarefa
        )
        tarefas.save()
        return redirect(reverse('adicionar'))
    
    tarefas = Tarefas.objects.all()
    return render(request, 'tarefas.html', context = {'tarefas': tarefas})

def deletar(request, id):
    tarefa = get_object_or_404(Tarefas, id = id)
    tarefa.delete()
    return redirect(reverse('adicionar'))

def editar(request, id):
    if request.method == "POST":
        tarefa = get_object_or_404(Tarefas, id = id)
        editada = request.POST.get('tarefa')
        tarefa.tarefa = editada
        tarefa.save()
        return redirect(reverse('adicionar'))
    return render(request, 'editar.html') 