# Generated by Django 3.0.3 on 2020-03-18 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0002_ansimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='ansmodel',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
