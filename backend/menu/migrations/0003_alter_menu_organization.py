# Generated by Django 4.1.1 on 2022-09-11 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menu_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.organization'),
        ),
    ]
