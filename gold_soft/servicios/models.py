from django.db import models

class Servicio(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name