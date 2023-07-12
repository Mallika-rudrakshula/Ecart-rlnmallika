"""Ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from user import views as v
from admins import views as v1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name='index'),
    path('register/', v.register, name='register'),
    path('login/', v.login, name='login'),
    path('home/', v.home, name='home'),
    path('products/', v.products, name='products'),
    path('products/,<int:id>/', v.products, name='products'),
    path('uaccount/', v.uaccount, name='uaccount'),

    path('viewprofile/', v.profile, name='profile'),
    path('ahome/', v1.ahome, name='ahome'),
    path('alogin/', v1.alogin, name='alogin'),
    path('addproducts/', v1.addproducts, name='addproducts'),
    path('viewproducts/', v1.viewproducts, name='viewproduct'),
    path('buyproducts', v.buyproducts, name='buyproducts'),
    path('buyproducts/<int:id>/buy/', v.buyproducts, name='buyproducts'),
    path('upurchase/', v.upurchase, name='upurchase'),
    path('apurchase/', v1.apurchase, name='apurchase'),
    path('ulogout/', v.ulogout, name='ulogout'),
    path('alogout/', v1.alogout, name='alogout'),
    path('contact/', v.contact, name='contact'),
    path('furniture/',v.furniture,name='furniture'),
    path('digitalproducts/',v.digitalproducts,name='digitalproducts'),
    path('clothiong',v.clothing,name='clothing'),
    path('household',v.household,name='household'),
    path('inpro/',v.inpro,name='inpro'),
    path('buy/',v.buy,name='buy'),
    path('extra/',v.extra,name='extra'),
    path('extra/<int:id>/',v.extra,name='extra'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
