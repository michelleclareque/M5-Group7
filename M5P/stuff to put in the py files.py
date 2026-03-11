#views.py
from django.shortcuts import render
from .models import Supplier
from .models import WaterBottle

def view_suppliers(request):
    supplier_objects = Supplier.objects.all()
    return render(request, "MyInventoryApp/all_suppliers.html", {'suppliers':supplier_objects})

def view_waterbottles(request):
    waterbottle_objects = WaterBottle.objects.all()
    return render(request, "MyInventoryApp/all_waterbottles.html", {'watterbottles':waterbottle_objects})

def add_waterbottle(request):
    return render(request, "MyInventoryApp/add_waterbottle.html")

#urls.py
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('basic_list', views.view_basic_list, name='view_basic_list'),
]
#url py. add_menu