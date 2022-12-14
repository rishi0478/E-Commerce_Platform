"""EcommercePlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from App import views
from rest_framework.routers import DefaultRouter
# Creating Router Object
router = DefaultRouter()

# Reigister Router
router.register("Register_Product",views.UserProduct,basename='E-Commerce-Product')


urlpatterns = [
    path('api/',include(router.urls)),      # this path deal wit api router links
    path('',views.home_Page,name='home'),
    path('Products/<str:slug>',views.Products,name='products'),
    path('mycart/',views.Add_to_cart,name='add_cart'),
    path('remove_cart/<int:pk>',views.RemoveCart,name='remove_cart'),
    path('Reigstration-forms',views.RegisterUser,name='register'),
    path('Sign-in-page',views.login_user,name='login'),
    path('log-out',views.Logout,name='log'),
    path("All-Products",views.All_products_data , name="all_products"),
    path('checkout-products',views.Checkout_page,name='check'),
    path("update",views.UpdateQuantity,name="quantity")
]
