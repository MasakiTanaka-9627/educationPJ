# Generated by Django 3.0.3 on 2020-03-08 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('board_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='board.BoardModel')),
            ],
        ),
    ]
