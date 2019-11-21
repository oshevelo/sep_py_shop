from django.urls import path
from . import views


urlpatterns = [
    path('', views.Payment_list.as_view(), name='Payment_List'),
    path('payment_id/<int:payment_id>/', views.Payment_Detail.as_view(), name='Payment_Details'),
]
