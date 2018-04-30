from django.db import models
from django.urls import reverse
from django.conf import settings
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=False)
    message = models.TextField()

    def get_absolute_url (self):
        return reverse('post_detail',args=[self.post_id])