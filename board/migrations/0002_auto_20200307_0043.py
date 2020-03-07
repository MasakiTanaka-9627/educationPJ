# Generated by Django 3.0.3 on 2020-03-07 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 3, 7, 0, 43, 23, 967202), verbose_name='登録日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
