from django.db import models
from django.contrib.auth.models import User
# Create your models here.

delivery_choices = (
    ("Order Received", "Order Received"),
    ("Printed", "Printed"),
    ("Shipped","Shipped"),
    ("Delivered","Delivered")
)


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_status = models.BooleanField()
    delivery_status = models.CharField(max_length=15,choices=delivery_choices,default="Order Received")
    date = models.DateField(auto_now_add=True)
    total_price = models.FloatField()
    college = models.TextField(max_length=30)
    def __str__(self):
        return str(self.id)
    
class OrderDetails(models.Model):
    order_id = models.ForeignKey("Orders", on_delete=models.CASCADE)
    product_id = models.ForeignKey("shop.Products", on_delete=models.CASCADE)
    file_upload= models.FileField(upload_to='customer_files')
    pages = models.IntegerField()
    quantity = models.IntegerField()
    colour = models.IntegerField(blank=True,null=True)
    sides = models.IntegerField(blank = True,null=True)
    sub_total = models.FloatField()
    status = models.TextField(max_length=10)
    def __str__(self):
        return str(self.order_id)

class Payments(models.Model):
    id = models.OneToOneField(Orders, on_delete=models.CASCADE,primary_key=True)
    order_id = models.TextField(unique=True)
    payment_id = models.TextField(unique=True)
    signature = models.TextField()

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey("shop.Products", on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to="cart_files")
    pages = models.IntegerField(blank=True,null=True)
    sides = models.IntegerField(blank=True,null=True)
    quantity = models.IntegerField()
    colour = models.IntegerField(blank=True,null=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.user_id)
    