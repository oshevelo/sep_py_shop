
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'shipments'

urlpatterns = [
    path('', views.ShipmentList.as_view(), name='shipment_list'),
    path('<str:public_id>/', views.ShipmentDetails.as_view(), name='shipment_details'),
]