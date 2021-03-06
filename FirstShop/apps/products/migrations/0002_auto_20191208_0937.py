# Generated by Django 2.2.4 on 2019-12-08 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_can_be_sold',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_avaliable_count',
            new_name='avaliable_count',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_created_updated',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_detail',
            new_name='detail',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Number_of_pages',
            new_name='number_of_pages',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Publication_date',
            new_name='publication_date',
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Complect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('detail', models.TextField(default='')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=2, null=True)),
                ('products', models.ManyToManyField(to='products.Product')),
            ],
        ),
    ]
