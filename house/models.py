from django.db import models

# Create your models here.
class House(models.Model):
    name=models.CharField(max_length=100)
    build_year=models.CharField(default=2020)
    type=models.CharField(default='simple')

    def __str__(self):
        return self.name

