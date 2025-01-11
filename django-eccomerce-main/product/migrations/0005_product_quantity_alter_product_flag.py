# Generated by Django 4.1.5 on 2023-01-31 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='flag',
            field=models.CharField(choices=[('Sale', 'Sales'), ('Feature', 'Feature'), ('New', 'New')], max_length=20, verbose_name='flag'),
        ),
    ]
