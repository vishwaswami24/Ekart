from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CAT=((1,'Tubelight'),(2,'Fan'),(3,'Bulb'))
    name=models.CharField(max_length=50)
    price=models.FloatField()
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    pdetails=models.CharField(max_length=100,verbose_name="Product Details")
    is_active=models.BooleanField(default=True)
    pimage=models.ImageField(upload_to="image")

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    userid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='userid')    
    qty=models.IntegerField(default=1)

class Order(models.Model):
    orderid=models.CharField(max_length=50)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    userid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='userid')    
    qty=models.IntegerField(default=1)   
    amt=models.FloatField(default=0) 

class OrderHistory(models.Model):
    orderid=models.CharField(max_length=50)
    pid=models.ForeignKey(Product,on_delete=models.CASCADE,db_column='pid')
    userid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='userid')    
    qty=models.IntegerField(default=1)   
    amt=models.FloatField(default=0)
    date=models.DateTimeField(auto_now_add=True)  
    
class UserInfo(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='userid') 
    gender=models.CharField(max_length=10)
    mobile=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    pincode=models.IntegerField(default=1)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)

