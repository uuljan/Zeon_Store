# Generated by Django 3.2.7 on 2022-06-07 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bestseller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='novelty',
        ),
    ]
