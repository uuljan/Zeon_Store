# Generated by Django 3.2.7 on 2022-06-09 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20220608_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderinfo', to='orders.order'),
        ),
    ]
