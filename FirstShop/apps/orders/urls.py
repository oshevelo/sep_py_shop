from django.urls import path
from . import views


urlpatterns = [
    path('', views.Order_List_Create.as_view(), name='Order_List_Create'),
    path('<int:order_id>/', views.Order_Detail.as_view(), name='Order_Detail'),
    path('l/', views.Order_Item_List_Create.as_view(), name='Order_Item_List_Create'),
    path('d/<int:order_item_id>/', views.Order_Item_Detail.as_view(), name='Order_Item_Detail'),
]
