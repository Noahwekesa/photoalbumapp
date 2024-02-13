from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"


class Photo(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    Category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    image = models.ImageField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
