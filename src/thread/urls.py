from django.urls import re_path
from rest_framework.routers import DefaultRouter

from thread.api import ThreadAPISet

router = DefaultRouter()
router.register(r"", ThreadAPISet, basename="thread")
urlpatterns = router.urls


# Define a separate URL pattern for the endpoint that requires pk validation

# This code validates that pk are positive integers and conform to the expected format.
# If they don't conform, Django will automatically return a 404 error.

urlpatterns += [
    re_path(
        r"^(?P<pk>\d+)/$",
        ThreadAPISet.as_view({"delete": "destroy"}),
        name="thread-detail",
    ),
]
