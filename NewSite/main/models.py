from django.db import models
from PIL import Image

# Create your models here.

class Media(models.Model):

    class Meta:
        verbose_name_plural = "Media"

    timestamp = models.DateTimeField()
    image = models.ImageField(upload_to="media")
    url = models.URLField()
    order = models.IntegerField(default=0)
    visable =

    def __str__(self):
        return self.image.url

