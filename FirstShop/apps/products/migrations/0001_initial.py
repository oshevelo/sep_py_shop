# Generated by Django 2.2.4 on 2019-11-17 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField(default=0)),
                ('product_avaliable_count', models.PositiveIntegerField(default=0, null=True)),
                ('product_detail', models.TextField(default='')),
                ('product_can_be_sold', models.BooleanField(default=True)),
                ('product_created_updated', models.DateTimeField(auto_now_add=True)),
                ('Publication_date', models.DateTimeField()),
                ('Number_of_pages', models.IntegerField(default=0)),
            ],
        ),
    ]
