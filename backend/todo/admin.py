from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "user",
    )
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Todo, TodoAdmin)