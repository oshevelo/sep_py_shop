# Generated by Django 2.2.6 on 2019-12-18 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0005_auto_20191124_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='invoice_id',
            field=models.CharField(default=None, max_length=200, null=True, verbose_name='Document Number'),
        ),
    ]
