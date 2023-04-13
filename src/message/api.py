from django.http import JsonResponse
from rest_framework import status

from message.serializers import MessageSerializer
from shared.django import (
    CreateListViewSet,
    CustomPagination,
    ResponceMultiSerializer,
    ResponceSerializer,
)
from thread.models import Thread


class MessageAPISet(CreateListViewSet):
    serializer_class = MessageSerializer
    lookup_field = "thread_id"
    lookup_url_kwarg = "thread_id"
    pagination_class = CustomPagination

    def get_queryset(self):
        thread_id = self.kwargs[self.lookup_field]
        thread = Thread.objects.get(id=thread_id)

        return thread.messages.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response = ResponceMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response = ResponceSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

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

        page = self.paginate_queryset(messages)

        if page is not None:
            serializer = self.get_serializer(page, many=True)

            return self.get_paginated_response(serializer.data)

        serializer = self.serializer_class(messages, many=True)
        response = ResponceMultiSerializer({"results": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_200_OK)
