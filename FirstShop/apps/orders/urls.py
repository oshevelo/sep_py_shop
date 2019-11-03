from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.Order_List.as_view(), name='Order_List'),
    path('details/<int:order_id>/', views.Order_Detail.as_view(), name='Order_Detail'),
]