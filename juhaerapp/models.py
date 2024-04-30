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
    
class Bookinglog(models.Model):
    item = models.CharField(max_length= 100)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.item 
