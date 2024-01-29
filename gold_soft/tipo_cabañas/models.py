from django.db import models

class Tipo_cabaña(models.Model):
    id = models.CharField(primary_key=True,max_length=10)
    name = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name