from .forms import *
from .views import *
from django.urls import path

urlpatterns = [
    path('signup',SignUp.as_view(),name='signup'),
    path('logout',LgOut.as_view(),name='logout'),
]
