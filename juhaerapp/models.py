from django.db import models

class Equipment(models.Model):
    name= models.CharField(max_length=100)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    device_type = models.CharField(max_length=100)
    device_serial = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    gpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

