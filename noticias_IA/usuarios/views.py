from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

def registro(request):
    if request.user.is_authenticated:
        return redirect('lista_articulos')
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Bienvenido, {username}! Te has registrado exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Error en el registro. Por favor, verifica los datos.')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('lista_articulos')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}!')
                return redirect('lista_articulos')
            else:
                messages.error(request, 'Usuario o contraseña incorrecta.')
        else:
            messages.error(request, 'Usuario o contraseña incorrecta.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('lista_articulos')

