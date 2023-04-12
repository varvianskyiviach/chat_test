from django.conf import settings
from django.db import models

from thread.models import Thread


class Message(models.Model):
    sender = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )
    thread = models.ForeignKey(to=Thread, on_delete=models.CASCADE, related_name="messages")

    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message {self.id}"
