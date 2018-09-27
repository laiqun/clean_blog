from django.db import models
from blog.models import Post


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    post = models.ForeignKey(Post)

    def __str__(self):
        return self.content[:20]
