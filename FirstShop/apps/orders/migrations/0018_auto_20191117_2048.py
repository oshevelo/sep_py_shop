# Generated by Django 2.2.4 on 2019-11-17 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20191117_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='orders.OrderItem'),
        ),
    ]
