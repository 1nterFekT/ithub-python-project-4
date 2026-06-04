from django.db import models
from django.db.models import UniqueConstraint
from students.models import Group

class Discipline(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название дисциплины'
    )

    duration = models.PositiveIntegerField(
        verbose_name='Длительность'
    )

    curriculum = models.FileField(
        upload_to='curriculums/',
        null=True,
        blank=True,
        verbose_name='Учебный план'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        null=True,
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'
        ordering = ['-updated_at', '-created_at']
        indexes = [
            models.Index(fields=['title']),
            models.Index(fields=['updated_at']),
        ]

    def __str__(self):
        return self.title
    

class Course(models.Model):
    code = models.CharField(
        max_length=15,
        verbose_name='Код курса'
    )

    about = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name='Описание'
    )

    course_start = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата начала'
    )

    course_end = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата завершения'
    )

    discipline = models.ForeignKey(
        'courses.Discipline',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses',
        verbose_name='Дисциплина'
    )

    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='courses',
        verbose_name='Учебная группа'
    )

    teacher = models.ForeignKey(
        'staff.Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='courses',
        verbose_name='Преподаватель'
    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['discipline__title']
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['course_start']),
            models.Index(fields=['course_end']),
        ]

    def __str__(self):
        return self.code
    
class Topic(models.Model):
    ordering_number = models.PositiveIntegerField(
        verbose_name='Порядковый номер'
    )

    title = models.CharField(
        max_length=50,
        verbose_name='Название темы'
    )

    content = models.TextField(
        verbose_name='Содержимое'
    )

    duration = models.PositiveIntegerField(
        verbose_name='Количество часов'
    )

    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='topics',
        verbose_name='Дисциплина'
    )

    class Meta:
        verbose_name = 'Учебная тема'
        verbose_name_plural = 'Учебные темы'
        ordering = ['discipline', 'ordering_number']
        constraints = [
            UniqueConstraint(
                fields=['ordering_number', 'discipline'],
                name='unique_topic_ordering_per_discipline'
            )
        ]

    def __str__(self):
        return f'{self.ordering_number}. {self.title}'