# Generated by Django 4.2.7 on 2023-11-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valueOfGoods', models.IntegerField()),
                ('deliverBefore', models.DateField()),
                ('distance', models.IntegerField()),
                ('transportFee', models.IntegerField()),
                ('serviceFee', models.IntegerField()),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
