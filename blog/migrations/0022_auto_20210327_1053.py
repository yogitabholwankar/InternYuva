# Generated by Django 3.1.5 on 2021-03-27 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20210327_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 27, 10, 53, 53, 742592, tzinfo=utc)),
        ),
    ]