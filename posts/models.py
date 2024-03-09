from django.db import models
from django_extensions.db.fields import AutoSlugField


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from="title")
    image = models.ImageField(
        upload_to="media/",
        blank=True,
        null=True,
    )
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ["-created"]
