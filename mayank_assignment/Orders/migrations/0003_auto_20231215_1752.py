# Generated by Django 3.2 on 2023-12-15 12:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.date(2023, 12, 15)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank='true', default=datetime.datetime(2023, 12, 15, 17, 52, 0, 314145)),
        ),
    ]