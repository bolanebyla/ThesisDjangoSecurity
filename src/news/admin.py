from django.contrib import admin
from . import models


@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('id', 'title',)
    list_filter = ('author',)
    readonly_fields = ('creation_date', 'update_date')
