from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    #path('payment_l/', views.Payment_list.as_view(), name='Payment_List'),
    #path('payment_d/<int:order_id>/', views.Payment_Detail.as_view(), name='Payment_Detail'),
]
