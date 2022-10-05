from django.db import models
from PIL import Image, ExifTags
from slugger import AutoSlugField
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    facebook = models.CharField(max_length=300, blank=True, null=True)
    instagram = models.CharField(max_length=300, blank=True, null=True)
    linkedin = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return str(self.user)



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
    copyright_info = models.CharField(max_length=200, null=True, blank=True,)
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

    timestamp = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="media")
    order = models.IntegerField(default=0)
    visable = models.BooleanField(default=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    meta = models.TextField(max_length=2000, null=True, blank=True, editable=True)



    def save(self, *args, **kwargs):
        super(Media, self).save(*args, **kwargs)
        """Get EXIF"""
        im = Image.open(self.image)
        try:
            info = im.getexif()[0x010e]
            changed_info = info
            if self.meta == None:
                self.meta = info
                super(Media, self).save(*args, **kwargs)
            elif self.meta != None and changed_info != info:
                 self.meta = info
        except KeyError:
            pass
        super(Media, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Media"
        ordering = ['order']

    def __str__(self):
        return self.image.url



#BLOG STUFF

class BlogPost(models.Model):
    STATUS = (
        ('published', 'Published'),
        ('unpublished', 'Unpublished'),
    )

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique_for_date='publish')
    body = models.TextField()
    main_image = models.ForeignKey(Media, on_delete=models.CASCADE, null=True)
    post_images = models.ManyToManyField(Media, related_name="Blog_images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    edited = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default='unpublished')

    def __str__(self):
        return str(self.author) + " Blog Title: " + self.title

    def get_absolute_url(self):
        return reverse('blogs')
