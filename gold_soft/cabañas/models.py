from django.db import models

class Cabaña(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/cabaña_images', null=True)
    capacity = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    # type_cabin = models.ForeignKey('tipo_cabañas.Tipo_cabaña', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)

def __str__(self):
      return self.name