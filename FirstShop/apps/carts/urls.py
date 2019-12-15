from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cart_List.as_view(), name='Cart_List'),
    path('<int:cart_id>/', views.Cart_Detail.as_view(), name='Cart_Detail'),

]