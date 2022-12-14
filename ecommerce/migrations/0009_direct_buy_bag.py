# Generated by Django 3.2.8 on 2022-03-10 04:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_our_video'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0008_order_tracking_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direct_buy_bag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(default=1, max_length=100)),
                ('gst_amount', models.IntegerField(blank=True, null=True)),
                ('total_price', models.IntegerField(blank=True, null=True)),
                ('payable_price', models.IntegerField(blank=True, null=True)),
                ('add_date', models.DateField(auto_now=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Deactive'), ('3', 'Delete')], default=1, max_length=50)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.product')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
