# Generated by Django 3.2.7 on 2022-06-23 04:20

import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('image_collection', models.ImageField(upload_to='products', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('vendor', models.CharField(max_length=150, unique=True, verbose_name='Артикул')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('price_with_discount', models.IntegerField(blank=True, null=True, verbose_name='Цена со скидкой')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Процент скидки')),
                ('description', models.TextField(verbose_name='Описание')),
                ('structure', models.CharField(max_length=150, verbose_name='Состав ткани')),
                ('line', models.IntegerField(default=5, verbose_name='Количество в линейке')),
                ('fabric', models.CharField(max_length=150, verbose_name='Материал')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.collection')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='ImageProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products', verbose_name='Фотография')),
                ('color', colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=18, samples=[('#BED5D2', '#BED5D2'), ('#D6EEC4', '#D6EEC4'), ('#002B73', '#002B73'), ('#AC8549', '#AC8549'), ('#BAC0F8', '#BAC0F8'), ('#FDFDFD', '#FDFDFD'), ('#D3D3D2', '#D3D3D2'), ('#FF8888', '#FF8888')])),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_color', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite', models.BooleanField(default=False, verbose_name='Избранное')),
                ('quantity', models.PositiveSmallIntegerField(blank=True, default=1, null=True, verbose_name='Количествоизбранных товаров')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранные',
            },
        ),
    ]
