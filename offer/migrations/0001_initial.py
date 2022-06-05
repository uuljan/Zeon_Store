# Generated by Django 3.2.7 on 2022-06-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Публичная оферта',
                'verbose_name_plural': 'Публичная оферта',
            },
        ),
    ]
