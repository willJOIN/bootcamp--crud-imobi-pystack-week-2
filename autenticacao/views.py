from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants


def cadastro(request):
    # Se entrar na página
    if request.method == "GET":
        return render(request, 'cadastro.html')
    # Se enviar no formulário
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')
        # Se campos do formulário estiverem vazios
        if len(username.strip()) == 0 or len(email.strip()) == 0 or len(password.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse nome cadastrado')
            return redirect('/auth/cadastro')

        try:
            user = User(username = username,
                        email = email,
                        password = password)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso')
            return redirect('/auth/login')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('auth/cadastro')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        # Se usuário não estiver logado
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("senha")
        usuario = auth.authenticate(username = username,
                                    password = password)
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Nome de usuário ou senha inválidos')
            return redirect('/auth/login')
        else:
            auth.login(request, usuario)
            return redirect('/')
    

def sair(request):
    auth.logout(request)
    return redirect('/auth/login')
        