from django.contrib import admin
from .models import TodoModel

class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "author",
    )


admin.site.register(TodoModel, TodoAdmin)