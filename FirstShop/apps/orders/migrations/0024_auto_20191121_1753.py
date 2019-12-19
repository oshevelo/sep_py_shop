# Generated by Django 2.2.4 on 2019-11-21 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0023_merge_20191121_1733'),
    ]

    operations = []
    '''
#        migrations.RemoveField(
#            model_name='order',
#            name='date',
#        ),
#        migrations.RemoveField(
#            model_name='order',
#            name='delivery',
#        ),
#        migrations.AddField(
#            model_name='order',
#            name='date_of_order',
#            field=models.DateTimeField(auto_now_add=True, null=True),
#        ),
        migrations.AddField(
            model_name='order',
            name='date_of_paid',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.CharField(choices=[('CA', 'Cash'), ('CR', 'Credit'), ('PP', 'PrivatPay'), ('POP', 'Pay of parts'), ('POC', 'Pay of card')], default='CR', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('ACCEPTED_FOR_PROCESSING', 'Accepted for processing'), ('PROCESSING', 'Processing'), ('PAID', 'Paid'), ('DONE', 'Done')], default='AFP', max_length=100, null=True),
        ),
    ]
    '''