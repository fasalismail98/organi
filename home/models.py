from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    type = models.CharField(max_length=200, null=True)


class product(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='product_img/')
    quantity = models.IntegerField(null=True)
    price = models.IntegerField(null=True)
    addedby=models.CharField(max_length=200,null=True)




class checkout(models.Model):
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    pincode=models.IntegerField(null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(max_length=250)
    addedby=models.CharField(max_length=150,null=True)
    totalamount=models.IntegerField(null=True)






class cart(models.Model):
    name = models.CharField(max_length=128,null=True)
    image = models.ImageField(upload_to='product_img/')
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    total = models.IntegerField(null=True)
    createdby=models.CharField(max_length=150,null=True)
    addedby=models.CharField(max_length=150,null=True)

class order(models.Model):
    name = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='product_img/')
    price = models.FloatField(null=True)
    quantity = models.IntegerField(null=True)
    total = models.FloatField(null=True)
    createdby=models.CharField(max_length=128,null=True)
    addedby=models.CharField(max_length=150,null=True)
    status =models.BooleanField(default=False)

class blog(models.Model):
    title=models.CharField(max_length=100,null=True)
    news=models.CharField(max_length=600,null=False)
    image=models.ImageField(upload_to='blog_img/')


class profile(models.Model):
    username=models.CharField(max_length=200)
    productname = models.CharField(max_length=200)
    quantity = models.IntegerField(null=True)
    status=models.CharField(max_length=100)
    price=models.IntegerField(null=True)
    totalamount=models.IntegerField(null=True)



# # Create your models here.
