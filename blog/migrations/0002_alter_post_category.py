# Generated by Django 4.2.3 on 2023-07-15 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='Uncategorized', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='categories', to='blog.category'),
        ),
    ]
