from django.contrib import admin
from .models import Property, PropertiesImages, Place, Category, Property_review, Property_book

# Register your models here.


admin.site.register(Property)
admin.site.register(PropertiesImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(Property_book)
admin.site.register(Property_review)