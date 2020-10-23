from django.contrib import admin

from .models import Tags, Project


# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_updated')
    search_fields = ('name',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_created', 'date_updated')
    search_fields = ('name',)
