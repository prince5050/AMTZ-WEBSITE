# Generated by Django 3.2.8 on 2022-02-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_product_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_price',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
