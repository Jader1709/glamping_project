from django.db import models

class Cliente(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    name = models.CharField(max_length=255)
    document = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name