from django.contrib import admin
from .models import Post


# внешний вид страницы с данными Post в админке
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "updated", "timestamp"]  # поля таблицы
    list_display_links = ["id", "updated"]  # поля, на которые можно нажать, чтобы открыть подробности о статье
    list_editable = ["title"]  # поля, которые можно редактировать прямо из списка статей
    list_filter = ["updated", "timestamp"]  # фильтры в меню справа
    search_fields = ["title", "content"]  # поля, по которым можно искать

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)