from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    model=models.CharField(max_length=50)
    price=models.IntegerField(default=20000000)

    def __str__(self):
        return self.name