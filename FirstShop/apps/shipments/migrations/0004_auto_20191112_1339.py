# Generated by Django 2.2.6 on 2019-11-12 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0003_auto_20191111_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseshipment',
            name='status_change_date',
            field=models.DateTimeField(auto_now=True, verbose_name='status_change_date'),
        ),
    ]
