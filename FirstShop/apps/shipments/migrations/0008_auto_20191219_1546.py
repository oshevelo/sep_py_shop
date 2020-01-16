# Generated by Django 2.2.6 on 2019-12-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0007_auto_20191219_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipmentlog',
            name='is_processed',
        ),
        migrations.AddField(
            model_name='shipmentlog',
            name='response_status',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='shipmentlog',
            name='request',
            field=models.TextField(blank=True, null=True, verbose_name='Request'),
        ),
    ]
