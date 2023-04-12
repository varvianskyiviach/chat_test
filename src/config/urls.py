from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("thread/", include("thread.urls")),
    path("", include("message.urls")),
    path("auth/", include("authentication.urls")),
]
