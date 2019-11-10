from django.db import models


class Category(models.Model):
    """
    Model to create top and sub categories
    """
    category_name = models.CharField(max_length=25)
    # null true mean there can be main category that do not have any parent category
    # category_object.sub_category.all() shows all related child objects
    top_category = models.ForeignKey('self',
                                     null=True,
                                     related_name='sub_category',
                                     on_delete=models.CASCADE)

    class Meta:
        ordering = ['category_name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name
