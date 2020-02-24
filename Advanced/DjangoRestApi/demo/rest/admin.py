from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rest.models import Post
from rest.models import User


admin.site.register(Post)
admin.site.register(User)