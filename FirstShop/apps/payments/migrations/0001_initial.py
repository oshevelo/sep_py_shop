# Generated by Django 2.2.4 on 2019-11-12 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('amount', models.DecimalField(decimal_places=6, default=0, max_digits=16)),
                ('reason', models.CharField(max_length=100)),
            ],
        ),
    ]
