from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=True)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ("-is_completed", "content")

    def __str__(self):
        return self.content
