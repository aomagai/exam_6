from django.db import models
from django.utils import timezone


STATUS_CHOICES = [
    ('active', 'Активно'),
    ('blocked', 'Заблокировано')
]


class Guestbook(models.Model):
    author = models.CharField(max_length=40, null=False, blank=False, default='Unknown', verbose_name='Автор')
    email = models.EmailField(max_length=40, null=False, blank=False, verbose_name='Почта')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    publish_at = models.DateTimeField(verbose_name="Время публикации", blank=True, default=timezone.now)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new', verbose_name='Модерация')


    def __str__(self):
        return "{}. {}".format(self.pk, self.author)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'