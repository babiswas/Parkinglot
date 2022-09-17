# Generated by Django 2.2 on 2022-09-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_auto_20220909_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='state',
            field=models.CharField(choices=[('PARKED', 'Parked'), ('UNPARKED', 'Occupied')], default='UNPARKED', max_length=20),
        ),
    ]
