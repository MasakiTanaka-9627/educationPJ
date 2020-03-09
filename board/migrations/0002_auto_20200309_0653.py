# Generated by Django 3.0.3 on 2020-03-08 21:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardmodel',
            name='author',
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='authour',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1, verbose_name='登録日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boardmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]