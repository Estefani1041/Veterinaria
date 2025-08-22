from django.shortcuts import render, redirect
from .models import Personal
from .forms import PersonalForm 

from django.shortcuts import redirect, get_object_or_404, render


def gestionar_personal(request): 
    personal_list = Personal.objects.all()
    return render(request, 'personal/gestionar_personal.html', {'personal': personal_list}) # se obtiene todos los datos que se encuentran registrados 

def registrar_personal(request):
    if request.method == 'POST':
        form = PersonalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestionar_personal')  # vuelve a la lista de personal
        else:
            print(form.errors)
    else:
        form = PersonalForm()
    
    return render(request, 'personal/registrar_personal.html', {'form': form})

def eliminar_personal(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')  # obtiene todos los checkboxes seleccionados para realizar la eliminación
        Personal.objects.filter(id__in=ids).delete()
    return redirect('gestionar_personal')


def actualizar_personal(request, id):
    personal = Personal.objects.get(id=id)

    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=personal)
        if form.is_valid():
            form.save()
            return redirect('gestionar_personal')  # vuelve a la lista
        else:
            print(form.errors)
    else:
        form = PersonalForm(instance=personal)

    return render(request, 'personal/actualizar_personal.html', {'form': form, 'personal': personal})