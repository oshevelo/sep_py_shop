# Generated by Django 2.2.4 on 2019-11-02 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='comment',
        ),
    ]