

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('public_order_id', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=13, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('delivery_id', models.CharField(max_length=50, null=True)),
                ('payment', models.CharField(choices=[('Cash', 'Cash'), ('Credit', 'Credit'), ('PrivarPay', 'PrivarPay'), ('Pay_of_parts', 'Pay of parts'), ('Pay_of_card', 'Pay of card')], max_length=100, null=True)),
                ('status', models.CharField(choices=[('Accepted_for_processing', 'Accepted for processing'), ('Processing', 'Processing'), ('Paid', 'Paid')], max_length=100, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField(default=1, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
                ('discount', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
