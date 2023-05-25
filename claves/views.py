from django.shortcuts import render, redirect
from .models import Categoria, Item
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def index(request):
    return render(request, 'main.html')

@login_required(login_url='/login/')
def cats(request):
    return render(request, 'cats.html')


@login_required(login_url='/login/')
def items(request):
    tran=Item.objects.all()
    return render(request, 'items.html', {"itemkey":tran})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username = username, password=password)
            if user is not None:
                login(request, user)
                return redirect('nombrex')
    return render(request, 'accounts/login.html', {})
