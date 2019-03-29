from django.shortcuts import render, redirect
from . models import Computador
from . forms import ComputadorForm

def computador_list(request):
    computadores = Computador.objects.all()
    return render(request, 'computador/list.html', {'computadores':computadores})

def computador_show(request, computador_id):
    computador = Computador.objects.get(pk=computador_id)
    return render(request, 'computador/show.html', {'computador':computador})

def computador_form(request):
    if request.method == 'POST':
        form = ComputadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/gestao/')
        else:
            return render(request, 'computador/form.html', {'form':form})
    else:
        form = ComputadorForm()
        return render(request, 'computador/form.html', {'form':form})

def computador_delete(request, computador_id):
    pc = Computador.objects.get(pk=computador_id)
    pc.delete()
    return redirect('/gestao/')