from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length = 15)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="product_images")
    def __str__(self):
        return self.name
