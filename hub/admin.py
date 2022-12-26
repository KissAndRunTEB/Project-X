from django.contrib import admin

from hub.models import Post, MenuItem, Video, FastNews

# Register your models here.


admin.site.register(Post)

admin.site.register(FastNews)

admin.site.register(Video)

admin.site.register(MenuItem)