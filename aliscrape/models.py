from django.db import models
import uuid


class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True


class ScrapedProduct(BaseModel):
    title = models.CharField(max_length=300, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
