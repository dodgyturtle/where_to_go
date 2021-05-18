from django.db import models
from django.db.models.base import Model
from sort_order_field import SortOrderField


class Place(models.Model):
    place_title = models.CharField("Название места", max_length=200, db_index=True)
    description_short = models.TextField("Краткое описание", null=True, blank=True)
    description_long = models.TextField("Полное описание", null=True, blank=True)
    latitude = models.FloatField("Широта", null=True, blank=True)
    longitude = models.FloatField("Долгота", null=True, blank=True)

    def __str__(self):
        return self.place_title


class PlaceImage(models.Model):
    sort_order = SortOrderField("Sort")
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name="place_images",
        verbose_name="Место",
    )
    image_url = models.ImageField("Изображение места", upload_to="place_images")

    def __str__(self) -> str:
        return f"{ self.sort_order } {self.place.place_title}"
