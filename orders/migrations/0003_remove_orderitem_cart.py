# Generated by Django 3.2.7 on 2022-06-19 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20220619_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='cart',
        ),
    ]