from django.shortcuts import render
from django.views.generic import TemplateView,ListView,View,DetailView
from owner.models import ProductModel

# Create your views here.
class UserHomeView(ListView):
    template_name="userhome.html"
    model=ProductModel
    context_object_name="product"
    
# class ProductDetails(View):
#     def get(self,request,*args,**kwargs):
#         pid=kwargs.get("id")
#         data=ProductModel.objects.get(id=pid)
#         return render(request,"productdetails.html",{'data':data})
    
class ProductDetails(DetailView):
    template_name="productdetails.html"
    model=ProductModel
    context_object_name="product"
    pk_url_kwarg="id"