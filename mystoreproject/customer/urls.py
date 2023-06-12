from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('userhome',UserHomeView.as_view(),name='userhome'),
    path('pro/<int:id>',ProductDetails.as_view(),name='pro'),
    path('addcart/<int:id>',AddCartView.as_view(),name="acart"),
    path('lcart',CartListView.as_view(),name="lcart"),
    path('delcart/<int:id>',DeleteList.as_view(),name="delcart"),
    path('check/<int:cid>/<int:pid>',CheckOut.as_view(),name="check"),
    path('buynow/<int:pid>',BuyNow.as_view(),name="buynow"),
    path('myorder',OrderListView.as_view(),name="myorder"),
    path('myorder/cancel/<int:id>',cancelorder,name="cancel"),
]
