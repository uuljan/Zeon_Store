# Generated by Django 3.2.7 on 2022-06-19 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(null=True, verbose_name='Количество товаров')),
                ('cart_cost', models.IntegerField(blank=True, null=True)),
                ('total_cart_cost', models.IntegerField(blank=True, null=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lines', models.IntegerField(blank=True, null=True, verbose_name='Количество линеек')),
                ('product_quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество всех товаров')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='Стоимость')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Скидка')),
                ('total_cost', models.IntegerField(blank=True, null=True, verbose_name='Итого к оплате')),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
            ],
            options={
                'verbose_name': 'Детали корзины',
                'verbose_name_plural': 'Детали корзины',
            },
        ),
    ]
