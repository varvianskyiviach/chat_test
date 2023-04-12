from django.http import JsonResponse
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from message.serializers import MessageSerializer
from thread.models import Thread


class CreateListViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    pass


class MessageAPISet(CreateListViewSet):
    serializer_class = MessageSerializer
    lookup_field = "thread_id"
    lookup_url_kwarg = "thread_id"

    def get_queryset(self):
        thread_id = self.kwargs[self.lookup_field]
        thread = Thread.objects.get(id=thread_id)
        return thread.messages.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = {"result": serializer.data}
        return JsonResponse(response, status=status.HTTP_201_CREATED)

    def read(self, request, thread_id=None, pk=None):
        thread = Thread.objects.get(id=thread_id)
        message = thread.messages.get(pk=pk)
        message.is_read = True
        message.save()
        return JsonResponse({"status": "read"})

    def get_unread(self, request, thread_id=None):
        thread = Thread.objects.get(id=thread_id)
        user = request.user
        messages = thread.messages.filter(is_read=False, sender=user)
        serializer = self.serializer_class(messages, many=True)
        response = {"results": serializer.data}

        return JsonResponse(response, status=status.HTTP_200_OK)
