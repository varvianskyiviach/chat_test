from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.viewsets import ViewSet

from thread.models import Thread
from thread.serializers import ThreadSerializer
from users.models import User


class ThreadAPISet(ViewSet):
    serializer_class = ThreadSerializer

    def create(self, request):
        participants_ids = request.data.get("participants", [])
        if len(participants_ids) > 2:
            return JsonResponse(
                {"error": "A thread can have at most 2 participants."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        participants = User.objects.filter(id__in=participants_ids)

        thread = (
            Thread.objects.filter(participants__in=participants)
            .annotate(num_participants=Count("participants"))
            .filter(num_participants=len(participants))
            .first()
        )

        if thread:
            serializer = self.serializer_class(thread)
            response = {"result": serializer.data}
            return JsonResponse(response, status=status.HTTP_200_OK)
        else:
            thread = Thread.objects.create()
            for participant in participants:
                thread.participants.add(participant.id)
            serializer = self.serializer_class(thread)
            response = {"result": serializer.data}
            return JsonResponse(response, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk):
        thread = get_object_or_404(Thread, pk=pk)
        thread.delete()
        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        thread = Thread.objects.all()
        serializer = self.serializer_class(thread, many=True)
        response = {"results": serializer.data}
        return JsonResponse(response, status=status.HTTP_200_OK)
