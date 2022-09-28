# Generated by Django 3.2.8 on 2022-01-17 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='order_Id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.order'),
        ),
        migrations.AddField(
            model_name='order_product',
            name='order_Id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='ecommerce.order'),
        ),
    ]