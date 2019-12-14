
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'delivery_api'

urlpatterns = [
    path('', views.DeliveryList.as_view(), name='delivery_list'),
    path('<str:invoice_id>/', views.DeliveryTrack.as_view(), name='delivery_track'),
]