from rest_framework import serializers

from message.models import Message
from thread.models import Thread
from users.models import User


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["thread", "text", "sender"]

    def create(self, validated_data):
        request = self.context["request"]
        thread_id = request.parser_context["kwargs"]["thread_id"]
        thread = Thread.objects.get(id=thread_id)
        sender_id = request.data["sender"]
        sender = User.objects.get(id=sender_id)

        validated_data["thread"] = thread
        validated_data["text"] = request.data["text"]
        validated_data["sender"] = sender

        messages = Message(**validated_data)
        messages.save()

        return messages
