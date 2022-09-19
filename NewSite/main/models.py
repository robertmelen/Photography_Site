from django.db import models
from PIL import Image, ExifTags
from slugger import AutoSlugField
from django.urls import reverse


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, null=True)
    visable = models.BooleanField(default=False, help_text="Make visable to appear on gallery category menu")
    slug = AutoSlugField(populate_from='title')


    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return str(self.title)


class Albums(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True,
                                   help_text="Gallery description on gallery page")
    slug = AutoSlugField(populate_from='name')
    created = models.DateTimeField()
    visable = models.BooleanField(default=False)
    type = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ForeignKey('Media', on_delete=models.CASCADE)
    album_images = models.ManyToManyField('Media', related_name="album_pictures")

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('main:gallery_detail', args=[self.slug],)

class Media(models.Model):

    timestamp = models.DateTimeField()
    image = models.ImageField(upload_to="media")
    order = models.IntegerField(default=0)
    visable = models.BooleanField(default=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    meta = models.CharField(max_length=2000, null=True, blank=True, editable=True)



    def save(self, *args, **kwargs):
        super(Media, self).save(*args, **kwargs)
        """Get EXIF"""
        im = Image.open(self.image)
        try:
            info = im.getexif()[0x010e]
            changed_info = info
            if changed_info != info:
                self.meta = info
        except KeyError:
            pass
        super(Media, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Media"
        ordering = ['order']




    def __str__(self):
        return self.image.url



