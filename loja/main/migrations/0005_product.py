# Generated by Django 4.1.5 on 2023-01-18 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_marcas_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='product_img/')),
                ('slug', models.CharField(max_length=400)),
                ('detail', models.TextField()),
                ('specs', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.marca')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tamanho')),
            ],
        ),
    ]