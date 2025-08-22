from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm  # debes crear un formulario similar a PersonalForm

def gestionar_usuario(request):
    usuarios = Usuario.objects.select_related('id_personal', 'id_tipo').all()
    return render(request, 'usuario/gestionar_usuario.html', {'usuarios': usuarios})

def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            return redirect('gestionar_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'usuario/registrar_usuario.html', {'form': form})

def eliminar_usuario(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        Usuario.objects.filter(id__in=ids).delete()
    return redirect('gestionar_usuario')

def actualizar_usuario(request):
    if request.method == 'POST':
        ids = request.POST.getlist('ids')
        if len(ids) == 1:
            usuario_id = ids[0]
            return redirect('editar_usuario', id=usuario_id)
        else:
            return redirect('gestionar_usuario')

def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            if 'password' in form.cleaned_data and form.cleaned_data['password']:
                usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            return redirect('gestionar_usuario')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario/editar_usuario.html', {'form': form, 'usuario': usuario})
