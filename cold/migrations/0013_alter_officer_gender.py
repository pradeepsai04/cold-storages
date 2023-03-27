# Generated by Django 4.0.2 on 2023-02-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cold', '0012_officer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female'), ('o', 'others')], max_length=1),
        ),
    ]