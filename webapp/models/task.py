from django.db import models


class Task(models.Model):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Заголовок"
    )

    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Описание",
    )
    status = models.ForeignKey(
        'webapp.Status',
        related_name='tasks',
        verbose_name='Статус',
        on_delete=models.RESTRICT,
        blank=False
    )
    type = models.ForeignKey(
        'webapp.Type',
        related_name='tasks',
        verbose_name='Тип',
        on_delete=models.RESTRICT,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return f"{self.summary} - {self.description} - {self.status} - {self.type}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


