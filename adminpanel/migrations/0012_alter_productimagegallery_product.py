# Generated by Django 4.2.3 on 2023-07-10 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0011_alter_productvariation_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimagegallery',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='adminpanel.shopproduct'),
        ),
    ]
