from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               related_name="parent_category", blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            if Category.objects.filter(slug=slug).exists():
                unique_id = str(uuid.uuid4()).split('-')[0]
                self.slug = slugify(f'{self.name}-{unique_id}')
            else:
                self.slug = slug
        super(Category, self).save(*args, **kwargs)

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
        Category, on_delete=models.SET_DEFAULT, default='19e72906-51a2-4998-a0a1-aca503284bbd', related_name='category')
    tags = models.ManyToManyField(Tag, related_name='tags', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, default=1)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        words = (f"{self.description[:250]}....") if len(
            self.description) > 75 else self.description
        self.short_description = words

        if not self.slug:
            sluged = slugify(self.title)
            unique_number = str(uuid.uuid4()).split('-')
            unique_slug = f'{sluged}-{unique_number[0]}'

            if Post.objects.filter(slug=sluged).exists():
                self.slug = unique_slug
            else:
                self.slug = sluged

        super(Post, self).save(*args, **kwargs)


class Comment(BaseModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post', blank=True, null=True)
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name='commenter')
    comment = models.TextField(max_length=500)
    liked = models.IntegerField(blank=True, default=0)
    disliked = models.IntegerField(blank=True, default=0)
    replied = models.ForeignKey('self', on_delete=models.CASCADE,
                                blank=True, null=True, related_name='replied_comment')

    def __str__(self):
        return str( self.commenter.username +' ' + self.comment +' ' + self.post.title )
