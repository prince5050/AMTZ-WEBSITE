# Generated by Django 3.2.8 on 2022-01-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourCenter', '0008_ourservice_service_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourservice',
            name='service_pdf',
            field=models.FileField(blank=True, null=True, upload_to='uploads/Services/pdf'),
        ),
        migrations.AddField(
            model_name='ourservice',
            name='service_use1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourservice',
            name='service_use2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourservice',
            name='service_use3',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ourservice',
            name='service_use5',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
