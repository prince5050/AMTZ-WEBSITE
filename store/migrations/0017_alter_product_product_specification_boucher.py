# Generated by Django 3.2.8 on 2022-08-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20220317_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_specification_boucher',
            field=models.FileField(blank=True, max_length=500, null=True, upload_to='uploads/products/specification'),
        ),
    ]
