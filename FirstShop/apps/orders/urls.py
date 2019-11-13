from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('order_lc/', views.Order_List_Create.as_view(), name='Order_List_Create'),
    path('order_d/<int:order_id>/', views.Order_Detail.as_view(), name='Order_Detail'),
]