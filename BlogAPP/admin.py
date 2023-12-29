from django.contrib import admin
from .models import blogs

# Register your models here.
class blogform(admin.ModelAdmin):
    list_display = ['id', 'created', 'title', 'content', 'updated']
admin.site.register(blogs, blogform)
