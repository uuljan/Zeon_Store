# Generated by Django 3.2.7 on 2022-06-06 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_tab', '0006_imagequestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagequestion',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='tab_images'),
        ),
    ]
