# Generated by Django 2.2.4 on 2019-11-14 10:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_merge_20191114_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='top_category',
            field=models.ForeignKey(help_text='Enter a book top category (e.g. Language, Genre)', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_category', to='catalog.Category'),
        ),
    ]
