from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    blog_title = models.CharField(max_length=1000)
    user_id = models.IntegerField()
    blog_text = models.TextField()

    def __str__(self):
        return self.blog_title