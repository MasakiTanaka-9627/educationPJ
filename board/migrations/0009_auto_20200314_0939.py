# Generated by Django 3.0.3 on 2020-03-14 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_boardimage_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardimage',
            name='board',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.BoardModel'),
        ),
    ]
