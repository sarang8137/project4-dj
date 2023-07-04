from django.urls import path
from .views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("product",ProductViewsetView,basename="product")
router.register("user",SignUpView,basename="userreg")
router.register("productmv",ProductModelViewset,basename="pmv")

urlpatterns = [
    path('prod',ProductsView.as_view()),
    path('token',views.obtain_auth_token)
    # path('products<int:id>',ProductsView.as_view()),
]+router.urls

#localhost:8000/owner/product/
#localhost:8000/owner/product/1/
