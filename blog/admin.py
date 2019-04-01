from django.contrib import admin
from .models import Post, Status, Member, Tag

class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_time', 'status', 'deadline',]

admin.site.register(Post, PostAdmin,)
admin.site.register(Tag,)
admin.site.register(Member,)
admin.site.register(Status,)
