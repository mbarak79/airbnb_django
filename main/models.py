from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


class Property(models.Model):
    name       = models.CharField(max_length=100)
    price       = models.PositiveIntegerField(default=0)
    rating      = models.PositiveIntegerField()
    description = models.TextField(max_length=12000)
    place       = models.ForeignKey('Place', related_name=("property_place"), on_delete=models.CASCADE)
    image       = models.ImageField(upload_to='Propertires/')
    category    = models.ForeignKey('Category', related_name="property_category", on_delete=models.CASCADE)
    created_at  = models.DateTimeField(default=timezone.now)
    slug        = models.SlugField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug': self.slug})
    



class PropertiesImages(models.Model):
    properies = models.ForeignKey(Property, related_name=("property_images"), on_delete=models.CASCADE)
    image     = models.ImageField(upload_to='Property_images/')

    def __str__(self):
        return str(self.properies)


class Place(models.Model):
    name    = models.CharField(max_length=50)
    image   = models.ImageField(upload_to='Places/')

    def __str__(self):
        return self.name


class Category(models.Model):
    name    = models.CharField( max_length=50)
    slug    = models.SlugField(blank=True, null=True)
    icon    = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('home:index', kwargs={'slug': self.slug})

    



class Property_review(models.Model):
    author      = models.ForeignKey(User, related_name="author_review", on_delete=models.CASCADE)
    property    = models.ForeignKey(Property, related_name="property_review", on_delete= models.CASCADE)
    rate        = models.PositiveIntegerField(default=0)
    feedback    = models.TextField(max_length=2000)
    created_at  = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.property)

COUNT = (
    ( 0, 0 ),
    ( 1, 1 ),
    ( 2, 2 ),
    ( 3, 3 ),
    ( 4, 4 ),
)

class Property_book(models.Model):
    user      = models.ForeignKey(User, related_name="book_owner", on_delete=models.CASCADE, default=1)
    property    = models.ForeignKey(Property, related_name="property_book", on_delete= models.CASCADE)
    date_from   = models.DateTimeField(default=timezone.now)
    date_to     = models.DateTimeField(default=timezone.now)
    guest       = models.IntegerField(default=1, choices=COUNT)
    children    = models.IntegerField(default=0, choices=COUNT)


    def __str__(self):
        return str(self.property)


