# Generated by Django 3.1.5 on 2021-04-04 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dprocess', '0003_orders_updateorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='zip_code',
        ),
    ]
