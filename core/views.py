from django.shortcuts import render

from django.shortcuts import render, redirect
from usuario.models import Usuario 


def login(request):
    if request.method == 'POST':
        usuario_input = request.POST.get('usuario')
        password_input = request.POST.get('password')

        try:
            user = Usuario.objects.get(usuario=usuario_input)
            if user.check_password(password_input):
                # Guardamos la sesión
                request.session['usuario_id'] = user.id
                request.session['usuario_tipo'] = user.id_tipo.cargo
                return redirect('home')  #home donde se ven las demás opciones 
            else:
                error = "La contraseña que ingresate es incorrecta"
        except Usuario.DoesNotExist:
            error = "Este usuario no exixte"

        return render(request, 'core/login.html', {'error': error})

    return render(request, 'core/login.html')

def home(request):
    if 'usuario_id' not in request.session:
        return redirect('login') 
    return render(request, 'core/home.html')

def cerrar_sesion(request):
    request.session.flush()
    return redirect('login')
