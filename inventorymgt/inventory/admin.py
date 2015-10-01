from django.contrib import admin

# Register your models here.
from .models import Item, Category

admin.site.register(Category)
admin.site.register(Item)
