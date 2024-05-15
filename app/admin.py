from django.contrib import admin
from app.models import Post


class MainModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'voice', 'video')
    search_fields = ('title',)
    ordering = ('-created_at',)


admin.site.register(Post, MainModelAdmin)
