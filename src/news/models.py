from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    author = models.ForeignKey(User, on_delete=models.PROTECT)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-update_date', '-creation_date']

    def __str__(self):
        return f'[{self.id}] {self.title}'

    def get_absolute_url(self):
        return reverse('news:update', kwargs={'pk': self.id})
