# Generated by Django 4.2.3 on 2023-07-15 10:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent_category', to='blog.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=70)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=350)),
                ('description', models.TextField(max_length=5000)),
                ('short_description', models.TextField(blank=True, max_length=400)),
                ('slug', models.SlugField(blank=True, max_length=400, unique=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='blog-images')),
                ('category', models.ForeignKey(default='Uncategorized', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='category', to='blog.category')),
                ('tags', models.ManyToManyField(blank=True, related_name='tags', to='blog.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
