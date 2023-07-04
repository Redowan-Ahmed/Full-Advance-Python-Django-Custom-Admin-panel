# Generated by Django 4.2.3 on 2023-07-04 13:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0005_shopproduct_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopproduct',
            name='slug',
            field=models.SlugField(blank=True, default=uuid.uuid4, max_length=350, unique=True),
        ),
    ]