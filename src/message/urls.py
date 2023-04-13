from django.urls import re_path

from message.api import MessageAPISet

# This code validates that thread_id and pk are positive integers and conform to the expected format.
# If they don't conform, Django will automatically return a 404 error.

urlpatterns = [
    re_path(
        r"^thread/(?P<thread_id>\d+)/message/$",
        MessageAPISet.as_view({"post": "create", "get": "list"}),
    ),
    re_path(
        r"^thread/(?P<thread_id>\d+)/message/(?P<pk>\d+)/read$",
        MessageAPISet.as_view({"put": "read"}),
    ),
    re_path(
        r"^thread/(?P<thread_id>\d+)/messages/unread$",
        MessageAPISet.as_view({"get": "get_unread"}),
    ),
]
