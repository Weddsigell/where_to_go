from django.db import models
from django.core.validators import MinLengthValidator
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        verbose_name='Название места',
        max_length=300,
        validators=[
            MinLengthValidator(3, 'Название должно быть от 3 до 300 символов')
        ],
    )
    description_short = HTMLField(
        verbose_name='Краткое описание',
        max_length=1000,
    )
    description_long = HTMLField(
        verbose_name='Полное описание',
        max_length=5000,
    )
    lng = models.FloatField(
        verbose_name='Долгота',
    )
    lat = models.FloatField(
        verbose_name='Широта',
    )
    

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['title']


    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    image = models.ImageField(
        verbose_name='Картинка',
        upload_to='.'
    )
    position = models.IntegerField(
        verbose_name='Позиция',
        default=0
    )
    place = models.ForeignKey(
        Place,
        verbose_name='Место',
        related_name='imgs',
        on_delete=models.CASCADE
    )


    class Meta:
        verbose_name = 'Каринка'
        verbose_name_plural = 'Картинки'
        ordering = ['position']


    def __str__(self):
        return f'{self.place.title}'
