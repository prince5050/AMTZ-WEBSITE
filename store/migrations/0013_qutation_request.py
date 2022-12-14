# Generated by Django 3.2.8 on 2022-02-19 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_delete_qutation_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qutation_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('Product_name', models.CharField(blank=True, max_length=250, null=True)),
                ('fullname', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=50, null=True)),
                ('subject', models.CharField(blank=True, max_length=250, null=True)),
                ('message', models.TextField(default='')),
                ('quantity', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
