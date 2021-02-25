from django.db import models


class Grammar(models.Model):
    grammar_title = models.CharField(max_length=255)  # заголовок
    grammar_text = models.TextField(max_length=100000)  # текст

    def __unicode__(self):
        return self.grammar_title

    def get_absolute_url(self):
        return "/grammar/%i/" % self.id