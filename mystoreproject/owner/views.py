from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import ProductSerializer,UserSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from rest_framework.response import Response
from .models import ProductModel
from rest_framework.decorators import action
from rest_framework import authentication,permissions


# Create your views here.
class ProductsView(APIView):
    def post(self,request,*args,**kwargs):
        ser=ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def get(self,request,*args,**kwargs):
        pro=ProductModel.objects.all()
        ser=ProductSerializer(pro,many=True)
        return Response(data=ser.data)
    def delete(self,request,*args,**kwargs):
        ProductModel.objects.filter(id=kwargs.get("id")).delete()
        return Response({"msg":"Deleted"})
    def put(self,request,*args,**kwargs):
        pro=ProductModel.objects.get(id=kwargs.get('id'))
        ser=ProductSerializer(data=request.data,instance=pro)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Updated"})
        return Response({"msg":"Filed"})
    

class ProductViewsetView(ViewSet):   

    def list(self,request,*args,**kwargs):
        prod=ProductModel.objects.all()
        ser=ProductSerializer(prod,many=True)
        return Response(data=ser.data)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get(id=id)
        prod=ProductModel.objects.all()
        ser=ProductSerializer(prod)
        return Response(data=ser.data)
    def create(self,request,*args,**kwargs):
        ser=ProductSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prod=ProductModel.objects.get(id=id)
        ser=ProductSerializer(data=request.data,instance=prod)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        ProductModel.objects.filter(id=id).delete()
        return Response({"msg":"Deleted"})
    
    @action(methods=["GET"],detail=False)
    def category(self,request,*args,**kwargs):
        cat=ProductModel.objects.values_list("product_category",flat=True).distinct()
        return Response(data=cat)


class ProductModelViewset(ModelViewSet):
    serializer_class=ProductSerializer
    queryset=ProductModel.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        ProductModel.objects.filter(id=id).delete()
        return Response({"msg":"Deleted"})
    

class SignUpView(ViewSet):
    def create(self,request,*args,**kwargs):
        ser=UserSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"OK"})
        return Response(data=ser.errors)

