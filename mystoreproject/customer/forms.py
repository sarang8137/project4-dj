from django import forms
from .models import Cart

class Cartform(forms.ModelForm):
    class Meta:
        model=Cart
        fields=["quantity"]
        widgets={
            "quantity":forms.NumberInput(attrs={"class":"form-control","min":1})
        }