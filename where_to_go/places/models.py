import json
import os


from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    slug = models.SlugField(unique=True, null=True)
    place_title = models.CharField("Название места", max_length=200, db_index=True)
    description_short = models.TextField("Краткое описание", null=True, blank=True)
    description_long = HTMLField("Полное описание", null=True, blank=True)
    latitude = models.FloatField("Широта", null=True, blank=True)
    longitude = models.FloatField("Долгота", null=True, blank=True)

    def __str__(self):
        return self.place_title

    class Meta:
        verbose_name = "Место отдыха"
        verbose_name_plural = "Места отдыха"


class PlaceImage(models.Model):
    sort_order = models.IntegerField("Sort", default=0, blank=False, null=False)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="place_images",
        verbose_name="Место",
    )
    image_url = models.ImageField("Изображение места", upload_to="place_images")

    class Meta(object):
        ordering = ["sort_order"]
        verbose_name = "Изображение места отдыха"
        verbose_name_plural = "Изображение мест отдыха"

    def __str__(self) -> str:
        return f"{ self.sort_order } {self.place.place_title}"
