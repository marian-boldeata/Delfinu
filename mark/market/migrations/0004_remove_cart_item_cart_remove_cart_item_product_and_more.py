# Generated by Django 5.0.6 on 2024-06-06 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_cart_cart_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cart_item',
        ),
    ]