from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import BarangForm, GudangForm, KasirForm
from .models import Barang, Gudang, Kasir
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def home(request):
    context ={
        'title' : "Menu",
    }
    return render(request, 'menu.html',context)

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            messages.success(request, "Registration successful. Please log in.")
            return redirect('login')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

def kasir(request):
    if request.method == 'POST':
        form = KasirForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Penjualan berhasil disimpan!")
            return redirect('kasir')  # Redirect ke halaman gudang setelah submit
    else:
        form = KasirForm()
    
    # Query semua data Gudang
    kasir_list = Kasir.objects.all()
    
    context = {
        'form': form,
        'title' : 'Kasir',
        'kasir_list': kasir_list,
    }
    return render(request, 'kasir.html', context)

def gudang(request):
    if request.method == 'POST':
        form = GudangForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Data gudang berhasil disimpan!")
            return redirect('gudang')  # Redirect ke halaman gudang setelah submit
    else:
        form = GudangForm()
    
    # Query semua data Gudang
    gudang_list = Gudang.objects.all()
    
    context = {
        'form': form,
        'title' : 'Gudang',
        'gudang_list': gudang_list,
    }
    return render(request, 'gudang.html', context)

def pembukuan(request):
    kasir_list = Kasir.objects.all()
    gudang_list = Gudang.objects.all()
    barang_list = Barang.objects.all()

    context ={
        'title' : "Pembukuan",
        'gudang_list': gudang_list,
        'kasir_list' : kasir_list, 
        'barang_list': barang_list,
    }
    return render(request, 'pembukuan.html',context)

def inputdata(request):
    if request.method == 'POST':
        form = BarangForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Barang berhasil diinput!")  # Tambahkan pesan sukses
            return redirect('inputdata')  # Redirect ke halaman yang sama setelah menyimpan
    else:
        form = BarangForm()
    
    # Ambil semua data barang

    # Susun konteks
    context = {
        'title': "Input Data",
        'form': form,
    }
    
    return render(request, 'inputdata.html', context)

