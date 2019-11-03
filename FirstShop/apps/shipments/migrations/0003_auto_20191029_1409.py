# Generated by Django 2.2.6 on 2019-10-29 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0002_shipment_shipment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='shipment_status',
            field=models.IntegerField(choices=[('POD', 'Payment on delivery'), ('INP', 'Instant Payment'), ('CTC', 'Card to Card payment'), ('CTF', 'Certificate payment')], default=1),
        ),
    ]
