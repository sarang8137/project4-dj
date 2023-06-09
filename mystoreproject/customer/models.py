from django.db import models
from owner.models import ProductModel
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default="cart")

    @property
    def totalamt(self):
        cnt=self.product.product_price*self.quantity
        return cnt
    
class Orders(models.Model):
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField(max_length=500)
    phone=models.IntegerField()
    options=(
        ("order placed","order placed"),
        ("shipped","shipped"),
        ("out for delivery","out for delivery"),
        ("cancel","cancel")
    )
    status=models.CharField(max_length=100,choices=options,default="order placed")
    date=models.DateField(auto_now_add=True,null=True)
