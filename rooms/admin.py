from collections.abc import Sequence
from typing import ClassVar

from django.contrib import admin

from .models import Category, Room, Task


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    prepopulated_fields: ClassVar[dict[str, Sequence[str]]] = {
        "slug": ("name",),
    }


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    prepopulated_fields: ClassVar[dict[str, Sequence[str]]] = {
        "slug": ("title",),
    }


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):  # pyright: ignore[reportMissingTypeArgument]
    list_display = (
        "title",
        "room",
        "task_type",
        "points",
        "order",
        "enabled",
    )

    list_filter = (
        "task_type",
        "enabled",
        "room",
    )

    search_fields = (
        "title",
        "description",
    )
