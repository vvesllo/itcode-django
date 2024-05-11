from django.db import models
from django.db.models import Count
from django.utils import timezone

# Create your models here.

class User(models.Model):

    PERMISSIONS = (
        ('user', 'Пользователь'),
        ('moderator', 'Модератор'),
        ('admin', 'Администратор'),
    )


    first_name = models.CharField('Имя', max_length=30, blank=False, null=False, default='')
    second_name = models.CharField('Фамилия', max_length=40, blank=False, default='')
    third_name = models.CharField('Отчество', max_length=30, blank=True, null=True)

    permission = models.CharField('Должность', max_length=10, choices=PERMISSIONS, blank=False, null=False, default='user')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.first_name} {self.second_name} ({self.permission})"


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField('Заголовок', blank=False, null=False, max_length=100)
    content = models.TextField('Текст', blank=False, null=False)

    post_date = models.DateField('Дата публикации', blank=False, null=False, default=timezone.now)


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f"{self.title} ({self.post_date})"
