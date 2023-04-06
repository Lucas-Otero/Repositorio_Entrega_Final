from django.db import models
from blog.models import Article

class Image(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.article.title + ' Image'
