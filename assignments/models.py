from django.core.exceptions import ValidationError
from django.db import models

from courses.models import Topic
from students.models import Student


class Assignment(models.Model):
    topic = models.OneToOneField(
        Topic,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assignment',
        verbose_name='Топик'
    )

    weight = models.PositiveIntegerField(
        verbose_name='Максимальный балл'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Контрольная точка'
        verbose_name_plural = 'Контрольные точки'
        ordering = [
            'topic__discipline',
            'topic__ordering_number'
        ]

    def __str__(self):
        return f'КТ: {self.topic}'


class Submission(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='submissions',
        verbose_name='Студент'
    )

    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.CASCADE,
        related_name='submissions',
        verbose_name='Контрольная точка'
    )

    answer = models.TextField(
        verbose_name='Ответ'
    )

    score = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Оценка'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = [
            'assignment__topic__discipline',
            'assignment__topic__ordering_number'
        ]

    def clean(self):
        if (
            self.score is not None
            and self.assignment
            and self.score > self.assignment.weight
        ):
            raise ValidationError({
                'score': 'Оценка не может превышать максимальный балл'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.student} -> {self.assignment}'