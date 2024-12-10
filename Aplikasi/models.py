# models.py
from django.db import models
    
class Barang(models.Model):
    nama_barang = models.CharField(max_length=100)
    harga = models.BigIntegerField()
    suplier = models.CharField(max_length=100)
    alamat = models.TextField()
    nomor_telepon = models.CharField(max_length=15)

    def __str__(self):
        return self.nama_barang

class Gudang(models.Model):
    nama_barang = models.CharField(max_length=100, verbose_name="Nama Barang")
    jumlah_barang_masuk = models.PositiveIntegerField(verbose_name="Jumlah Barang Masuk")
    jumlah_barang_terjual = models.PositiveIntegerField(verbose_name="Jumlah Barang Terjual")
    sisa_barang = models.PositiveIntegerField(verbose_name="Sisa Barang")
    tanggal_update = models.DateField(verbose_name="Tanggal Update")

    def __str__(self):
        return self.nama_barang

class Kasir(models.Model):
    nama_barang = models.CharField(max_length=100, verbose_name="Nama Barang")
    harga = models.PositiveIntegerField(verbose_name="Harga")
    quantity = models.PositiveIntegerField(verbose_name="Quantity")
    total = models.PositiveIntegerField(verbose_name="Total")

    def __str__(self):
        return self.nama_barang