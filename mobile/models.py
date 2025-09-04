from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    icon=models.CharField(max_length=50,blank=True)

    def __str__(self):
       return self.name

class costumer(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=50)

class products(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=6)
    storage=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    image=models.ImageField(upload_to='static/images')
    category=models.ForeignKey(category,on_delete=models.CASCADE)
   
    def __str__(self):
     return self.name
    
class Cart(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
   session_id=models.CharField(max_length=100,null=True,blank=True)
   product=models.ForeignKey(products,on_delete=models.CASCADE)
   quantity=models.PositiveBigIntegerField(default=1)
   created_at=models.DateTimeField(auto_now_add=True)
 
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    invoice_number = models.CharField(max_length=20)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
