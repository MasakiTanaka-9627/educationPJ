# Generated by Django 3.0.3 on 2020-03-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0009_auto_20200314_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardimage',
            name='title',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='title',
            field=models.CharField(max_length=25),
        ),
    ]