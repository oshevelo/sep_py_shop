from django.urls import path
from .views import ProductView, SingleProductView

app_name = 'products'
urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>/', SingleProductView.as_view())
]	