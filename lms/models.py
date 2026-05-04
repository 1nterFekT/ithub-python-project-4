from django.db import models


class Group(models.Model):
    title = models.CharField(unique=True, blank=False, verbose_name="Название")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f'<{self.pk}> {self.title}'
