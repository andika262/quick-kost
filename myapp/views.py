from django.shortcuts import redirect, render
from myapp.models import *
from .forms import AddKost
from .serializers import homeSerialzer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Berhasil Di buat!")
            return redirect('signup')
        else:
            messages.error(request, "Terjadi Kesalahan!")
            return redirect('signup')
    else:
        form = UserCreationForm()
        ctx = {
            'form' : form,
        }
    return render(request, 'signup.html',ctx)

@login_required(login_url=settings.LOGIN_URL)
def index(request):
    homes = home.objects.all() 
    
    kontent = {
        'homes' : homes
    }
    return render(request, 'home.html', kontent)

@login_required(login_url=settings.LOGIN_URL)
def add_kost(request, *args, **kwargs):
    if request.method == 'POST':
        form = AddKost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        form = AddKost()
        pesan = "Data Berhasil Ditambahkan!"
        ctx = {
            'form' : form,
            'pesan' : pesan
        }
        return render(request, 'add_kost.html', ctx)
    else:
        form = AddKost()
        ctx = {
            'form' : form,
        }
        print(form.errors)    
        return render(request, 'add_kost.html', ctx)
@login_required(login_url=settings.LOGIN_URL)
def update_kost(request,id_nama):
    homes = home.objects.get(id = id_nama)
    if request.POST:
        form = AddKost(request.POST, request.FILES, instance=homes)
        if form.is_valid():
            form.save()
            pesan = "Data Berhasil Diupdate!"
            ctx = {
                'form' : form,
                'pesan' : pesan,
                'homes' : homes
            }
            return render(request, 'update.html', ctx)    
    else:
        form = AddKost(request.FILES,instance=homes)
        ctx = {
            'form' : form,
            'homes' : homes
        }  
        return render(request, 'update.html', ctx) 
@login_required(login_url=settings.LOGIN_URL)
def delete_kost(request, id_nama):
    homes = home.objects.get(id = id_nama)
    homes.delete()

    return redirect("/home")

@login_required(login_url=settings.LOGIN_URL)
@api_view(['GET'])
def homesApi(request, *args, **kwargs):
    homes = home.objects.all()
    data = homeSerialzer(homes, many=True).data
    return Response(data)