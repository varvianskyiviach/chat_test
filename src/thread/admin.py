from django.contrib import admin

from thread.models import Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    filter_horizontal = ("participants",)
