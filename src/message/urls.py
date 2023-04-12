from django.urls import path

from message.api import MessageAPISet

urlpatterns = [
    path(
        "thread/<int:thread_id>/message/",
        MessageAPISet.as_view({"post": "create", "get": "list"}),
    ),
    path(
        "thread/<int:thread_id>/message/<int:pk>/read",
        MessageAPISet.as_view({"put": "read"}),
    ),
    path(
        "thread/<int:thread_id>/messages/unread",
        MessageAPISet.as_view({"get": "get_unread"}),
    ),
]
