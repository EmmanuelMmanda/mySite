from django.contrib import admin
from .models import Gallery,Tag,Post,Comment

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Gallery)
admin.site.register(Comment)