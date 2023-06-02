from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('userhome',UserHomeView.as_view(),name='userhome'),
    path('pro/<int:id>',ProductDetails.as_view(),name='pro'),

]
