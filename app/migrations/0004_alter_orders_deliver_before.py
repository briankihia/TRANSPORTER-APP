# Generated by Django 4.2.7 on 2023-11-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_deliverbefore_orders_deliver_before_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='deliver_before',
            field=models.DateField(null=True),
        ),
    ]
