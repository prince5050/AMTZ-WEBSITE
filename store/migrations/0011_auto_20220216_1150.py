# Generated by Django 3.2.8 on 2022-02-16 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_latest_notification_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latest_notification',
            old_name='discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='latest_notification',
            old_name='job_discription_pdf',
            new_name='job_description_pdf',
        ),
    ]
