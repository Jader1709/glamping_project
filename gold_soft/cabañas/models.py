from django.db import models

class Cabaña(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='gold_soft/static/images', null=True)
    capacity = models.DateField()
    price = models.IntegerField()
    description = models.TextField()
    id_type_cabin = models.ForeignKey('tipo_cabañas.Tipo_cabaña', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)

def __str__(self):
      return self.title