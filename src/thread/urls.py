from rest_framework.routers import DefaultRouter

from thread.api import ThreadAPISet

router = DefaultRouter()
router.register(r"", ThreadAPISet, basename="thread")
urlpatterns = router.urls
