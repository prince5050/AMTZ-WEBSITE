# Generated by Django 3.2.8 on 2021-11-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourCenter', '0003_auto_20211117_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center',
            name='center_image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/center/'),
        ),
        migrations.AlterField(
            model_name='center',
            name='center_video_key',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
