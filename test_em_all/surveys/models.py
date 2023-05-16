from django.db import models
from users.models import User

class Survey(models.Model):
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    subject = models.ForeignKey(
        "Дисциплина",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='surveys',
        verbose_name='Дисциплина',
        help_text='Выберите дисциплину'
    )
    title = models.TextField(
        'Название теста',
        help_text='Введите название теста'
    )
    question = models.ForeignKey(
        "Question",
    )
    # criterion

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    # title = models.CharField(max_length=200)
    text = models.TextField(
        'Текст вопроса',
        help_text='Введите текст вопроса'
    )
    number = models.CharField(max_length=9)

    def __str__(self):
        return self.title