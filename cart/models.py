from enum import unique
from tkinter import CASCADE
from django.db import models
from e_app.models import *

# Create your models here.
class Cartlist(models.Model):
    cart_id = models.CharField(max_length=250,unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.cart_id 

class ItemsFree(models.Model):
    productF = models.ForeignKey(ProductFree,on_delete=models.CASCADE)
    cart = models.ForeignKey(Cartlist,on_delete=models.CASCADE)
    quantF = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.productF)

    def total(self):
        return self.productF.price*self.quantF
   

# class ItemsPaid(models.Model):
#     productP = models.ForeignKey(ProductPaid,on_delete=models.CASCADE)
#     quantP = models.IntegerField()

# def __str__(self):
#     return self.productP