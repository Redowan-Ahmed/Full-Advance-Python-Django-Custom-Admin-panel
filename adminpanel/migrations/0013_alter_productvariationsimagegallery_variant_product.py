# Generated by Django 4.2.3 on 2023-07-11 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0012_alter_productimagegallery_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariationsimagegallery',
            name='variant_product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='variant_product_images', to='adminpanel.productvariation'),
        ),
    ]
