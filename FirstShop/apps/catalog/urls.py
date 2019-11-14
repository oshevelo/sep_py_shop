from django.urls import path

from apps.catalog import views

urlpatterns = [
    path('all-categories-list/', views.CategoryList.as_view(), name='all_categories_list')
]
