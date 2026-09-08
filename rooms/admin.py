from collections.abc import Sequence
from typing import ClassVar

from django.contrib import admin

from .models import Category, Room


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
