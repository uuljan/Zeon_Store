# Generated by Django 3.2.7 on 2022-06-19 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_favorite_user'),
        ('orders', '0004_auto_20220619_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='lines',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product_quantity',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='user',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='order_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Количество товаров'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='order',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Заказы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Заказы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Заказы'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('NEW', 'НОВЫЙ'), ('ISSUED', 'ОФОРМЛЕН'), ('CANCELED', 'ОТМЕНЕН')], default='NEW', max_length=55),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='Заказы'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_cost',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lines', models.IntegerField(blank=True, null=True, verbose_name='Количество линеек')),
                ('product_quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество всех товаров')),
                ('cost', models.IntegerField(blank=True, null=True, verbose_name='Стоимость')),
                ('discount', models.IntegerField(blank=True, null=True, verbose_name='Скидка')),
                ('total_cost', models.IntegerField(blank=True, null=True, verbose_name='Итого к оплате')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
            options={
                'verbose_name': ' Информация заказа',
                'verbose_name_plural': 'Информация заказа',
            },
        ),
    ]
