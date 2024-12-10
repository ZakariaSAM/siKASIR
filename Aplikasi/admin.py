from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Barang, Gudang, Kasir


class BarangAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_barang', 'harga', 'suplier', 'alamat', 'nomor_telepon')
    search_fields = ('nama_barang', 'suplier', 'alamat')
    list_filter = ('suplier',)
    ordering = ('id',)

# Mendaftarkan model Gudang ke Admin
class GudangAdmin(admin.ModelAdmin):
    # Konfigurasi untuk tampilan di admin panel
    list_display = ('nama_barang', 'jumlah_barang_masuk', 'jumlah_barang_terjual', 'sisa_barang', 'tanggal_update')
    search_fields = ('nama_barang',)  # Menambahkan fitur pencarian berdasarkan nama barang
    list_filter = ('tanggal_update',)  # Menambahkan filter berdasarkan tanggal update
    ordering = ('-tanggal_update',)  # Mengurutkan data berdasarkan tanggal terbaru

class KasirAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_barang', 'harga', 'quantity', "total")
    search_fields = ('nama_barang',)
    ordering = ('id',)

admin.site.register(Barang, BarangAdmin)
admin.site.register(Gudang,GudangAdmin)
admin.site.register(Kasir,KasirAdmin)