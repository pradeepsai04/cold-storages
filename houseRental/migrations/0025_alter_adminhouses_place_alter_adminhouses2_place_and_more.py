# Generated by Django 4.0.2 on 2022-08-15 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houseRental', '0024_alter_house_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminhouses',
            name='PLACE',
            field=models.TextField(default='VIZAG'),
        ),
        migrations.AlterField(
            model_name='adminhouses2',
            name='PLACE',
            field=models.TextField(default='VIZAG'),
        ),
        migrations.AlterField(
            model_name='adminhouses3',
            name='PLACE',
            field=models.TextField(default='VIZAG'),
        ),
    ]