# Generated by Django 3.0.3 on 2020-03-16 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
                ('ans', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ans.AnsModel')),
            ],
        ),
    ]
