from django.db import models


# from django.contrib.auth.models import User


# Create your models here.


class Address(models.Model):
    door_no = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    area = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)


class Consumer(models.Model):
    user_address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return str(self.email)


class Subsription(models.Model):
    choices = (('1', "500ml"), ('2', "1000ml"))
    user = models.OneToOneField(Consumer , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    milk_choices = models.CharField(choices=choices, default='1', max_length=1)

    def __str__(self):
        return str(self.user.name)