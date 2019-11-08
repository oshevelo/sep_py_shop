
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shipments'

urlpatterns = [
    path('', views.ShipmentList.as_view(), name='shipment_list'),
    path('index/', views.index, name='index'),
    path('s/<str:public_order_id>', views.ShipmentDetails.as_view(), name='shipment_details'),
]
