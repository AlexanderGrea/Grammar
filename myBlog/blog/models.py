from django.db import models


class Post(models.Model):  # заменить на Grammar
    title = models.CharField(max_length=120)
    description = models.TextField(default='Описание')
    keywords = models.CharField(max_length=120, default='Ключевые слова')   # убрать
    image = models.FileField(null=True, blank=True)                         # убрать
    content = models.TextField()
    visible = models.BooleanField(default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)       # убрать
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)     # убрать

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/" % (self.id)

    class Meta:
        ordering = ["-id", "-timestamp"]