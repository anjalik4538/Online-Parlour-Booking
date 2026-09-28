from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=50)
    price = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.name
