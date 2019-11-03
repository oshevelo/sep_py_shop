from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('order_l/', views.Order_List.as_view(), name='Order_List'),
    path('order_d/<int:order_id>/', views.Order_Detail.as_view(), name='Order_Detail'),
]