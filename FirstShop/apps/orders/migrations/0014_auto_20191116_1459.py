# Generated by Django 2.2.4 on 2019-11-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_auto_20191114_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='public_id',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
