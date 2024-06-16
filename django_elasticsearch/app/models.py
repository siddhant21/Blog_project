from django.db import models
from django.contrib.auth.models import User

# class Book(models.Model):
#     title = models.CharField(max_length=1000)
#     author = models.CharField(max_length=1000)
#     description = models.TextField()

#     def __str__(self):
#         return self.title

class Blog(models.Model):
    blog_title = models.CharField(max_length=1000)
    user_id = models.IntegerField()
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_text = models.TextField()

    def __str__(self):
        return self.blog_title