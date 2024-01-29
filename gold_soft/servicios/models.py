from django.db import models

class Servicio(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name