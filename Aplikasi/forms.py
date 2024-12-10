# forms.py
from django import forms
from .models import Barang, Gudang, Kasir

class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        fields = ['nama_barang', 'harga', 'suplier', 'alamat', 'nomor_telepon']
        widgets = {
            'nama_barang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Barang'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga'}),
            'suplier': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Suplier'}),
            'alamat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alamat'}),
            'nomor_telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nomor Telepon'}),
        }

class GudangForm(forms.ModelForm):
    class Meta:
        model = Gudang
        fields = ['nama_barang', 'jumlah_barang_masuk', 'jumlah_barang_terjual', 'sisa_barang', 'tanggal_update']
        widgets = {
            'nama_barang': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nama Barang',
            }),
            'jumlah_barang_masuk': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jumlah Barang Masuk',
            }),
            'jumlah_barang_terjual': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jumlah Barang Terjual',
            }),
            'sisa_barang': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Sisa Barang',
            }),
            'tanggal_update': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
        }

class KasirForm(forms.ModelForm):
    class Meta:
        model = Kasir
        fields = ['nama_barang', 'harga', 'quantity', 'total']
        widgets = {
            'nama_barang': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama Barang'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Harga'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'quantity'}),
            'total': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'total'}),
        }