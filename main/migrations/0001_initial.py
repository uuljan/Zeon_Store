# Generated by Django 3.2.7 on 2022-06-23 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='Иконка')),
                ('title_advantage', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description_advantage', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Наши преимущества',
                'verbose_name_plural': 'Наши преимущества',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='carusel-img', verbose_name='Фотография')),
                ('main_url', models.URLField(blank=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдер',
            },
        ),
        migrations.CreateModel(
            name='Novelty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novelty', models.BooleanField(default=False, verbose_name='Новинка')),
                ('item1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
            ],
            options={
                'verbose_name': 'Новинка',
                'verbose_name_plural': 'Новинки',
            },
        ),
        migrations.CreateModel(
            name='Bestseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestseller', models.BooleanField(default=False, verbose_name='Хит продаж')),
                ('obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='best', to='product.product')),
            ],
            options={
                'verbose_name': 'Хит продаж',
                'verbose_name_plural': 'Хиты продаж',
            },
        ),
    ]