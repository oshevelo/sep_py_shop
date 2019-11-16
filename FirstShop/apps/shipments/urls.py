
from django.urls import path
from . import views

app_name = 'shipments'

urlpatterns = [
    path('', views.ShipmentList.as_view(), name='shipment_list'),
    path('<int:public_order_id>/', views.ShipmentDetails.as_view(), name='shipment_details'),
]
