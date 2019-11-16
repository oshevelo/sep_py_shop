from django.urls import path
from .views import BookView, SingleBookView

app_name = 'products'
urlpatterns = [
    path('', BookView.as_view()),
    path('<int:pk>/', SingleBookView.as_view())
]	