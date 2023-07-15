from django.db import models
from django.utils.text import slugify
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=128, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name="parent_category", blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=70)

    def __str__(self) -> str:

        return self.name


class Post(BaseModel):
    title = models.CharField(max_length=350)
    description = models.TextField(max_length=5000)
    short_description = models.TextField(max_length=400, blank=True)
    slug = models.SlugField(max_length=400, blank=True, unique=True)
    thumbnail = models.ImageField(
        upload_to='blog-images', blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_DEFAULT, default='Uncategorized', related_name='category')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.short_description:
            words = (f"{self.description[:250]}....") if len(
                self.description) > 75 else self.description
            self.short_description = words

        if not self.slug:

            sluged = slugify(self.title)
            unique = Post.objects.filter(slug=sluged)

            if unique.exists():
                unique_number = str(uuid.uuid4()).split('-')
                unique_slug = f'{sluged}-{unique_number[0]}'
                self.slug = unique_slug

            self.slug = sluged

        super(Post, self).save(*args, **kwargs)
