from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def SignupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Erro ao cadastrar')
    else:
        form = UserCreationForm()
    
    return render(request, 'auth/signup.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blueprint_A')
            else:
                return render(request, 'auth/login.html', {'error': 'Usuário ou senha inválidos.'})
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})
def LogoutView(request):
    logout(request)
    return redirect('home')  # Irá voltar à página inicial

