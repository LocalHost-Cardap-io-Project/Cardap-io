# Generated by Django 4.1.1 on 2022-09-10 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='author',
        ),
    ]
