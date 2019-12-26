from apps.products.models import Product
from django.db import models


class Category(models.Model):
    """
    Model to create top and sub categories
    """
    category_name = models.CharField(max_length=25,
                                     help_text='Enter a book category (e.g. Classic)')
    # null true mean there can be main category that do not have any parent category
    # category_object.sub_category.all() shows all related child objects
    top_category = models.ForeignKey('self',
                                     null=True,
                                     # used to make field optional in admin
                                     blank=True,
                                     related_name='sub_category',
                                     on_delete=models.CASCADE,
                                     help_text='Enter a book top category (e.g. Language, Genre)')

    indx = models.IntegerField(default=0,
                               help_text='Specify index number for sorting order')

    products = models.ManyToManyField(Product, related_name='categories')

    class Meta:
        # Sorting index from smaller to higher e.g. 1 top 2 second etc
        ordering = ['indx']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
