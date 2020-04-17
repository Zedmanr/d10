from django.db import models
from django.utils import timezone

TRANSMISSION_TYPE = [
    (1, "механика"),
    (2, "автомат"),
    (3, "робот"),
]


class Car(models.Model):
    manufacturer = models.CharField('Производитель', max_length=30, null=True)
    model_of_auto = models.CharField('Модель авто', max_length=40, null=True)
    year_of_issue = models.IntegerField('Год выпуска', default=timezone.now().year, null=True)
    transmission = models.SmallIntegerField('Коробка передач', choices=TRANSMISSION_TYPE, null=True)
    colour = models.CharField('Цвет', max_length=20, null=True)

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'

    def __str__(self):
        return f"Компания: {self.manufacturer}, модель: {self.model_of_auto}."
