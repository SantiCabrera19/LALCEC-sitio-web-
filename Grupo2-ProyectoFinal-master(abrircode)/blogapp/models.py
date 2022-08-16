from telnetlib import STATUS
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title