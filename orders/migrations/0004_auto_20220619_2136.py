# Generated by Django 3.2.7 on 2022-06-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_remove_orderitem_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='order_cost',
            new_name='cost',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='discount',
            field=models.IntegerField(blank=True, null=True, verbose_name='Скидка'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='lines',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество линеек'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='product_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='Количество всех товаров'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='total_cost',
            field=models.IntegerField(blank=True, null=True, verbose_name='Итого к оплате'),
        ),
        migrations.DeleteModel(
            name='OrderInfo',
        ),
    ]