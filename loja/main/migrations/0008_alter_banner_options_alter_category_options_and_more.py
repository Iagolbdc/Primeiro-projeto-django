# Generated by Django 4.1.5 on 2023-01-20 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_banner_remove_product_price_productattribute'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='banner',
            options={'verbose_name_plural': '1. Banners'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '2. Categories'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': '3. Colors'},
        ),
        migrations.AlterModelOptions(
            name='marca',
            options={'verbose_name_plural': '5. Marcas'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '6. Products'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': '7. ProductAttributes'},
        ),
        migrations.AlterModelOptions(
            name='tamanho',
            options={'verbose_name_plural': '4. Sizes'},
        ),
    ]
