# Generated by Django 3.2.8 on 2022-02-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20220117_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tracking_id',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]