from django.forms.models import BaseModelForm
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from django.http import HttpResponse
from django.contrib import messages
from .forms import Loginform,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.models import User

# Create your views here.

def sign_required(fun):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fun(request,*args,**kwargs)
        else:
            messages.warning(request,"login required for this action")
            return redirect("signin")
    return inner

class HomeView(TemplateView):
    template_name="home.html"

# class SignIn(View):
#     def get(self,request,*args,**kwargs):
#         form=Loginform()
#         return render(request,'signin.html',{'form':form})
#     def post(self,request,*args,**kwargs):
#         signin_data=Loginform(data=request.POST)
#         if signin_data.is_valid():
#             uname=signin_data.cleaned_data.get('username')
#             pswd=signin_data.cleaned_data.get('password')
#             user=authenticate(request,username=uname,password=pswd)
#             if user:
#                 login(request,user)
#                 messages.success(request,'login success')
#                 return redirect('home')
#             else:
#                 messages.success(request,'login failed')
#                 return render(request,'signin.html',{'form':signin_data})
            
# class SignUp(View):
#     def get(self,request,*args,**kwargs):
#         form=RegisterForm()
#         return render(request,'signup.html',{'form':form})
#     def post(self,request,*args,**kwargs):
#         form=RegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Registration successful')
#             return redirect('signin')
#         else:
#             messages.success(request,'Registration failed')
#             return render(request,'signup.html',{'form',form})

class SignUp(CreateView):
    template_name='signup.html'
    form_class=RegisterForm
    model=User
    success_url=reverse_lazy("home")
    def form_valid(self, form):
        messages.success(self.request,"Registration Successful")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"Registration Failed")
        return super().form_invalid(form)
    
class SignIn(FormView):
    template_name="signin.html"
    form_class=Loginform
    def post(self,request,*args,**kwargs):
        signin_data=Loginform(data=request.POST)
        if signin_data.is_valid():
            uname=signin_data.cleaned_data.get('username')
            pswd=signin_data.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,'login success')
                return redirect('userhome')
            else:
                messages.success(request,'login failed')
                return render(request,'signin.html',{'form':signin_data})
            
    


@method_decorator(sign_required,name='dispatch')
class LgOut(View):
    def get(selg,request,*args,**kwargs):
        logout(request)
        return redirect("signin")