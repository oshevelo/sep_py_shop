# Generated by Django 2.2.4 on 2019-12-22 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_category_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='categories', to='products.Product'),
        ),
    ]
