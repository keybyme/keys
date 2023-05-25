from django.shortcuts import render
from .models import Categoria, Item

def index(request):
    return render(request, 'main.html')

def cats(request):
    return render(request, 'cats.html')

def items(request):
    tran=Item.objects.all()
    return render(request, 'items.html', {"itemkey":tran})
