# Generated by Django 3.2.7 on 2022-05-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20220526_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novelties',
            fields=[
                ('NoveltiesID', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='ArticleID')),
                ('image', models.ImageField(upload_to='products')),
                ('color', models.CharField(choices=[('1', 'aquamarine'), ('2', 'lightGreen'), ('3', 'tan'), ('4', 'saddleBrown'), ('5', 'lavender'), ('6', 'white'), ('7', 'grey'), ('8', 'red')], max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('price_without_discount', models.IntegerField(blank=True, null=True)),
                ('discount', models.IntegerField(blank=True, null=True)),
                ('size', models.CharField(max_length=20)),
                ('favorite', models.BooleanField(default=False)),
            ],
        ),
    ]
