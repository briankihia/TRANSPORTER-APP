# Generated by Django 4.2.7 on 2023-11-25 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='done',
        ),
    ]
