# Generated by Django 5.0.6 on 2024-06-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_alter_product_imagine_produs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='imagine_produs',
            field=models.ImageField(default='no_img_available.jpg', upload_to='imagini_produs/'),
        ),
    ]
