from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField('Имя', max_length=100)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.name} {self.id}"


class Article(models.Model):
    author_id = models.IntegerField('Автор')
    title = models.CharField('Заголовок', max_length=100)
    content = models.CharField('Текст', max_length=150)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return f"{self.title}"
