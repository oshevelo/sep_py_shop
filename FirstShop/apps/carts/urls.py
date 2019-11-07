from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart_l/', views.Cart_List.as_view(), name='Cart_List'),
    path('cart_d/<int:cart_id>/', views.Cart_Detail.as_view(), name='Cart_Detail'),

]