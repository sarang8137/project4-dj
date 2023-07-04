from rest_framework import serializers
from .models import ProductModel
from django.contrib.auth.models import User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields="__all__"
    def validate(self, attrs):
        price=attrs.get("product_price")
        if price<0:
            raise serializers.ValidationError("Invalid Error")
        return attrs
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
    
    def create(self, validated_data):
        #return User.objects.create_user(**validated_data)
        return User.objects.create_superuser(**validated_data)
    
    
