# Generated by Django 4.0.2 on 2023-04-20 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cold', '0017_alter_officer_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='mill',
            name='VIDEO',
            field=models.FileField(default='NULL', upload_to='videos/'),
        ),
    ]
