from django.contrib import admin

# Register your models here.
# tasks/admin.py
from django.contrib import admin
from .models import Project, control_vuelos, Task


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)

@admin.register(control_vuelos)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id_vuelo", "created_at")
    search_fields = ("id_vuelo","destino" )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "project", "status", "due_date")
    list_filters = ("status","project" )
    search_fields = ("tittle","description" )