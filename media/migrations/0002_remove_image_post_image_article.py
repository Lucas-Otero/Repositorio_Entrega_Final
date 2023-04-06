# Generated by Django 4.1.7 on 2023-04-06 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('media', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post',
        ),
        migrations.AddField(
            model_name='image',
            name='article',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.article'),
        ),
    ]
