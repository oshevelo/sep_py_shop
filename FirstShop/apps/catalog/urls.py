from django.urls import path

from apps.catalog import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='all_categories_list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('products/<int:pk>/', views.CategoryProductDetail.as_view())
]
