from django.conf import settings
from django.db import models


class Thread(models.Model):
    participants = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="threads",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Thread {self.id}"
