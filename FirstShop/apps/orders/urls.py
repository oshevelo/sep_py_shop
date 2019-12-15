from django.urls import path

from . import views


urlpatterns = [
    path('', views.Order_List_Create.as_view(), name='Order_List_Create'),
    path('<int:order_id>/', views.Order_Detail.as_view(), name='Order_Detail'),
    path('account/', views.OrderList.as_view(), name='OrderList'),


]