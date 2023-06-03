from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, GroupsPosts

admin.site.register(GroupsPosts)
admin.site.register(Post)