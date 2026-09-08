from __future__ import annotations

from datetime import datetime

from django.db import models


class Difficulty(models.TextChoices):
    EASY = "easy", "Easy"
    MEDIUM = "medium", "Medium"
    HARD = "hard", "Hard"


class Category(models.Model):
    name: models.CharField[str, str] = models.CharField(
        max_length=50,
        unique=True,
    )

    slug: models.SlugField[str, str] = models.SlugField(unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Room(models.Model):
    title: models.CharField[str, str] = models.CharField(
        max_length=100,
    )

    slug: models.SlugField[str, str] = models.SlugField(
        max_length=100,
        unique=True,
    )

    description: models.TextField[str, str] = models.TextField()

    category: models.ForeignKey[Category, Category] = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="rooms",
    )

    difficulty: models.CharField[str, str] = models.CharField(
        max_length=10,
        choices=Difficulty,
        default=Difficulty.EASY,
    )

    points: models.PositiveIntegerField[int, int] = models.PositiveIntegerField(
        default=0,
    )

    enabled: models.BooleanField[bool, bool] = models.BooleanField(
        default=False,
    )

    created_at: models.DateTimeField[datetime, datetime] = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at: models.DateTimeField[datetime, datetime] = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ("title",)

    def __str__(self) -> str:
        return self.title
