from django.db import models

# Create your models here.
class ProductModel(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    options=(
        ('Outfit','Outfit'),
        ('footwear','footwear'),
        ('Cosmetics','cosmetics'),
        ('Electronics','Electronics'),
        ('Kitchen Appliences','Kitchen Appliences'),
        ('Others','Others')
    )
    product_category=models.CharField(max_length=100,choices=options)
    product_image=models.ImageField(upload_to='pro_image')
    product_description=models.CharField(max_length=100)