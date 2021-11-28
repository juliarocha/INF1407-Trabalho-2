from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse_lazy
from .models import Request
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import LivrosModel2Form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Livros


def livrosListView(request):
    if request.method == 'GET':
        livros = Livros.objects.all()
        context = {'livros': livros, }
        return render(
            request,
            'livros/listaLivros.html',
            context)



def livroCreateView(request):
    if request.method == 'GET':
        context = { 'formulario': LivrosModel2Form, }
        return render(request,
        "livros/criaLivros.html", context)

    elif request.method == 'POST':
        formulario = LivrosModel2Form(request.POST)
        if formulario.is_valid():
            livro = formulario.save()
            livro.save()
            return redirect("/")


def livroUpdateView(request, pk):
    if request.method == 'GET':
        livro = Livros.objects.get(pk=pk)
        formulario = LivrosModel2Form(instance=livro)
        context = {'livro': formulario, }
        return render(request, 'livros/atualizaLivro.html', context)
    elif request.method == 'POST':
        livro = get_object_or_404(Livros, pk=pk)
        formulario = LivrosModel2Form(request.POST, instance=livro)
        if formulario.is_valid():
            livro = formulario.save()
            livro.save()
            return redirect("/")
        else:
            context = {'livro': formulario, }
            return render(request, 'livros/atualizaLivro.html', context)


def livroDeleteView(request, pk):
    if request.method == 'GET':
        livro = Livros.objects.get(pk=pk)
        context = {'livro': livro, }
        return render(
        request, 'livros/apagaLivro.html',
        context)
    elif request.method == 'POST':
        livro = Livros.objects.get(pk=pk)
        livro.delete()
        print("Removendo o livro", pk)
        return redirect("/")


def register(request):
    if request.method == 'POST':
        # cria um usuário
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Conta criada para usuário: ' + user)
            return redirect("/login/")
        else:
            context = {
                'form': form,
            }
            return render(request, 'accounts/register.html', context)
    else:
        # mostra o formulário
        form = UserCreationForm()
        context = {'form': form, }
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Usuário ou senha estão incorretos!")
            return render(request, "accounts/login.html")
    return render(request, "accounts/login.html")


def deleteUser(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            print(username)
            u = User.objects.get(username=username)
            u.delete()
        except:
            messages.error(request, f"Failed to delete user!")
            return render(request, "accounts/delete.html")
        return redirect("/")
    else:
        return render(request, 'accounts/delete.html')


def logoutUser(request):
    logout(request)
    return redirect("/")
