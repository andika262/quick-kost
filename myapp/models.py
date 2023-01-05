from django.db import models

# Create your models here.
class home(models.Model):
    nama       = models.CharField(max_length=300)
    harga      = models.CharField(max_length=300, null=True)
    alamat     = models.CharField(max_length=300, null=True)
    coordX     = models.FloatField(null=True)
    coordY     = models.FloatField(null=True)
    foto       = models.ImageField('Gambar', null=True, blank=True)
    keterangan = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.nama