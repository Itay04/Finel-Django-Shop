# Generated by Django 4.1.4 on 2022-12-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_cart_delete_buy_alter_orders_customerorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]