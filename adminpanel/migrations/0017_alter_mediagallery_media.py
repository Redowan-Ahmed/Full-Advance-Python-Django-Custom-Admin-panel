# Generated by Django 4.2.3 on 2023-07-12 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0016_mediagallery_delete_imagegallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediagallery',
            name='media',
            field=models.FileField(blank=True, upload_to='media-files/2023'),
        ),
    ]