from django.db import models
from accounts.models import User

class Group(models.Model):
    COURSE_CHOICES = [
        ('1', '1 курс'),
        ('2', '2 курс'),
        ('3', '3 курс'),
        ('4', '4 курс'),
    ]

    title = models.CharField(
        max_length=15,
        verbose_name='Название группы'
    )

    course = models.CharField(
        max_length=1,
        choices=COURSE_CHOICES,
        verbose_name='Курс'
    )

    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'
        ordering = ['course']
        indexes = [
            models.Index(fields=['course']),
        ]

    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя'
    )

    last_name = models.CharField(
        max_length=40,
        verbose_name='Фамилия'
    )

    middle_name = models.CharField(
        max_length=40,
        blank=True,
        null=True,
        verbose_name='Отчество'
    )

    account = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Аккаунт'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Учебная группа'
    )

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.last_name} {self.first_name}'