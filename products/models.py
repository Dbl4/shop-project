from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(max_length = 128, unique = True)
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length = 256)
    image = models.ImageField(upload_to = 'product_images', blank = True)
    description = models.CharField(max_length = 64, blank = True, null = True)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    quantity = models.PositiveIntegerField(default = 0)
    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'

    @staticmethod
    def get_items():
        #quantity__gt возращает значения больше чем 0
        return Product.objects.filter(quantity__gt=0).order_by('category','name')
