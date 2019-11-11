# Generated by Django 2.2.4 on 2019-11-10 08:50

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
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_id', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=50, null=True)),
                ('discount', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('amount', models.PositiveIntegerField(default=1, null=True)),
                ('provider', models.CharField(choices=[('Rozetka', 'Rozetka'), ('Буква', 'Буква'), ('Globalbook', 'Globalbook'), ('Букля', 'Букля'), ('Yakaboo', 'Yakaboo')], max_length=100, null=True)),
                ('cart_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='carts.Cart')),
            ],
        ),
    ]
