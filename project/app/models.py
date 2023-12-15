from django.db import models

class Posts(models.Model):
    title = models.CharField(max_length=50, verbose_name='Title')
    content = models.TextField(verbose_name='Content')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'