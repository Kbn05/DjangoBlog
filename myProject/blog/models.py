from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    pub_date = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ('-published',)
        indexes = [
            models.Index(fields=['published'], name='published_idx'),
        ]

    def __str__(self):
        return self.title
