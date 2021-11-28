from django.shortcuts import render
from .forms import UserModel2Form
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Request
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        # cria um usuário
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Conta criada para usuário: ' + user)
            return redirect("login")
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


def index(request):
    return render(request, "home.html")


def results(request):
    all_requests = Request.objects.all()
    context = {request.name: request.author for request in all_requests}
    context.update({request.name+'OBD': request.author for request in all_requests})
    print(context)
    return render(request, 'resultado.html', context)


def validateUsername(request):
    username = request.GET.get("username", None)
    print("username: ", username)
    resposta = {'existe':  User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(resposta)

