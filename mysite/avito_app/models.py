from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=32)

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    Product_image = models.ImageField(upload_to='products_images')
    price = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)