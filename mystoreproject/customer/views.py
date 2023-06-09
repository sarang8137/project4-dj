from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,View,DetailView,CreateView
from owner.models import ProductModel
from .forms import Cartform
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Cart,Orders
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


#decorator
def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"login required")
            return redirect("signin")
    return inner

dec=[signin_required,never_cache]

# Create your views here.
@method_decorator(dec,name='dispatch')
class UserHomeView(ListView):
    template_name="userhome.html"
    model=ProductModel
    context_object_name="product"
    
# class ProductDetails(View):
#     def get(self,request,*args,**kwargs):
#         pid=kwargs.get("id")
#         data=ProductModel.objects.get(id=pid)
#         return render(request,"productdetails.html",{'data':data})

@method_decorator(dec,name='dispatch')
class ProductDetails(DetailView):
    template_name="productdetails.html"
    model=ProductModel
    context_object_name="product"
    pk_url_kwarg="id"

@method_decorator(dec,name='dispatch')
class AddCartView(CreateView):
    template_name="addcart.html"
    form_class=Cartform
    # success_url=reverse_lazy("uh")

    def post(self,request,*args,**kwargs):
        form_data=Cartform(data=request.POST)
        if form_data.is_valid():
            form_data.instance.product=ProductModel.objects.get(id=kwargs.get("id"))
            form_data.instance.user=request.user
            form_data.save()
            messages.success(request,"Product added to Cart")
            return redirect("userhome")
        else:
            return render(request,"addcart.html",{"form":form_data})
            

@method_decorator(dec,name='dispatch')
class CartListView(TemplateView):
    template_name="cart-list.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['cart']=Cart.objects.filter(user=self.request.user,status="cart")
        return context

@method_decorator(dec,name='dispatch')   
class DeleteList(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Cart.objects.filter(id=id).delete()
        messages.success(request,"Item Deleted")
        return redirect("lcart")

@method_decorator(dec,name='dispatch')
class CheckOut(TemplateView):
    template_name="checkout.html"

    def post(self,request,*args,**kwargs):
        cid=kwargs.get("cid")
        pid=kwargs.get("pid")
        cart=Cart.objects.get(id=cid)
        prod=ProductModel.objects.get(id=pid)
        user=request.user
        quantity=cart.quantity
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        Orders.objects.create(product=prod,user=user,quantity=quantity,address=address,phone=phone)
        cart.status="order placed"
        cart.save()
        messages.success(request,"order placed")
        return redirect("userhome")

@method_decorator(dec,name='dispatch')      
class BuyNow(TemplateView):
    template_name="checkout.html"

    def post(self,request,*args,**kwargs):
        pid=kwargs.get("pid")
        prod=ProductModel.objects.get(id=pid)
        user=request.user
        address=request.POST.get("address")
        phone=request.POST.get("phone")
        Orders.objects.create(product=prod,user=user,address=address,phone=phone)
        messages.success(request,"order placed")
        return redirect("userhome")

@method_decorator(dec,name='dispatch')       
class OrderListView(ListView):
    template_name="orderslist.html"
    model=Orders
    context_object_name="order"
    def get_queryset(self):
        return Orders.objects.filter(user=self.request.user)

dec   
def cancelorder(request,id):
    ord=Orders.objects.get(id=id)
    ord.status="cancel"
    ord.save()
    messages.error(request,"order cancelled")
    return redirect("myorder")
        