# Generated by Django 3.0.3 on 2020-03-14 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0007_auto_20200314_0551'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardimage',
            name='board',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='board.BoardModel'),
            preserve_default=False,
        ),
    ]
