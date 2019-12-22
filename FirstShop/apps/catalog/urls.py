from apps.catalog import views
from django.urls import path

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='all_categories_list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('categories/products/', views.CategoryProductList.as_view())
]
