# Generated by Django 4.1.5 on 2023-05-17 00:08

from django.db import migrations, models
import orders.utils.genirite_code


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='code',
            field=models.CharField(default=orders.utils.genirite_code.genirite_code, max_length=12),
        ),
    ]
