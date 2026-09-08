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
        verbose_name_plural = "Categories"

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

    @property
    def total_points(self) -> int:
        return sum(
            task.points
            for task in Task.objects.filter(
                room=self,
                enabled=True,
            )
        )

    def __str__(self) -> str:
        return self.title


class TaskType(models.TextChoices):
    INFO = "info", "Information"
    ANSWER = "answer", "Answer"
    FLAG = "flag", "Flag"


class Task(models.Model):
    room: models.ForeignKey[Room, Room] = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    title: models.CharField[str, str] = models.CharField(
        max_length=100,
    )

    description: models.TextField[str, str] = models.TextField()

    task_type: models.CharField[str, str] = models.CharField(
        max_length=10, choices=TaskType, default=TaskType.ANSWER
    )

    answer: models.CharField[str, str] = models.CharField(
        max_length=255,
        blank=True,
    )

    points: models.PositiveIntegerField[int, int] = models.PositiveIntegerField(
        default=10,
    )

    order: models.PositiveIntegerField[int, int] = models.PositiveIntegerField(
        default=1,
    )

    hint: models.TextField[str, str] = models.TextField(
        blank=True,
    )

    enabled: models.BooleanField[bool, bool] = models.BooleanField(
        default=True,
    )

    class Meta:
        ordering = ("order",)

    def __str__(self) -> str:
        return self.title
