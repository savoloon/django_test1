from django.db import models


class Author(models.Model):
    name = models.CharField('Имя автора', max_length=128)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey('core.Author', on_delete=models.CASCADE, null=True, blank=True, related_name='books')
    name = models.CharField('Название', max_length=128)
    pages = models.IntegerField('Количество страниц', blank=True, null=True)
    genre = models.ForeignKey('core.Genre', on_delete=models.CASCADE, null=True, blank=True, related_name='books')

    class Meta:
        ordering = ['pages']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateField()
    book = models.ManyToManyField('core.Book')
