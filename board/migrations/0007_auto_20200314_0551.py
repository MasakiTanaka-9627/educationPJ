# Generated by Django 3.0.3 on 2020-03-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_boardimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='count_ans',
            field=models.IntegerField(null=True),
        ),
    ]