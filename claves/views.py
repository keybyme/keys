from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Categoria, Item, Contacto, Qrcode
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import ItemForm, ContactoForm, QrcodeForm,QrcodeForm2
import io
import pyqrcode
import base64
@login_required(login_url='/login/')
def index(request):
    return render(request, 'main.html')

@login_required(login_url='/login/')
def cats(request):
    return render(request, 'cats.html')


@login_required(login_url='/login/')
def items(request):
    tran=Item.objects.all().order_by("remarks")
    return render(request, 'items.html', {"itemkey":tran})

@login_required(login_url='/login/')
def contactos(request):
    tranco=Contacto.objects.all()
    return render(request, 'contactos.html', {"contactokey":tranco})

def edit_items(request, pk):
    tran=Item.objects.get(id=pk)
    form=ItemForm(request.POST or None, instance=tran)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('itemsx')
    return render(request, 'edit_item.html', {"form":form})

def edit_contactos(request, pk):
    tranco=Contacto.objects.get(id=pk)
    form=ContactoForm(request.POST or None, instance=tranco)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('contactosx')
    return render(request, 'edit_contacto.html', {"form":form})

def add_items(request):
    formx=ItemForm(request.POST or None)
    if request.method == 'POST':
        formx.save()
        return redirect('itemsx')
    return render(request, 'add_item.html', {"form":formx})

def add_contactos(request):
    formxy=ContactoForm(request.POST or None)
    if request.method == 'POST':
        formxy.save()
        return redirect('contactosx')
    return render(request, 'add_item.html', {"form":formxy})

def delete_items(request, pk):
    tran=Item.objects.get(id=pk)
    tran.delete()
    return redirect('itemsx')

def delete_contactos(request, pk):
    tranco=Contacto.objects.get(id=pk)
    tranco.delete()
    return redirect('contactosx')
    

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


def logout_user(request):
    logout(request)
    return redirect('login')

# def createQrcode(request):
#     formsx=QrcodeForm(request.POST, request.FILES or None)
#     if request.method=="POST":
#         if formsx.is_valid():
#             formsx.save
#             return redirect('nombrex')
#     return render(request, 'qrcode.html', {'qrform': formsx})


# def generate_qr_code(request):
#     if request.method == 'POST':
#         form = QrcodeForm2(request.POST)
#         if form.is_valid():
#             link = form.cleaned_data['link']
#             qr_code = pyqrcode.create(link)

#             # Generate the QR code image and save it to a BytesIO object
#             buffer = io.BytesIO()
#             qr_code.png(buffer, scale=5)
#             buffer.seek(0)

#             # Set the appropriate response headers for automatic download
#             response = HttpResponse(content_type='image/png')
#             response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
#             response['Content-Length'] = str(len(buffer.getvalue()))

#             # Write the image data to the response
#             response.write(buffer.getvalue())

#             return response
#     else:
#         form = QrcodeForm2()

#     return render(request, 'qrcode.html', {'form': form})

def generate_qr_code(request):
    if request.method == 'POST':
        form = QrcodeForm2(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            qr_code = pyqrcode.create(link)

            # Generate the QR code image and save it to a BytesIO object
            buffer = io.BytesIO()
            qr_code.png(buffer, scale=5)
            buffer.seek(0)

            # Encode the image data as base64
            image_data = base64.b64encode(buffer.getvalue()).decode()

            return render(request, 'qrcode.html', {'form': form, 'image_data': image_data})
    else:
        form = QrcodeForm2()

    return render(request, 'qrcode.html', {'form': form})
