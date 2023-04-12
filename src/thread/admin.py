from django.contrib import admin

from thread.models import Thread

# admin.site.register(Thread)


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    filter_horizontal = ("participants",)


# @admin.register(Thread)
# class ThreadAdmin(admin.ModelAdmin):
#     list_display = ("id", "participants_list", "created", "updated")

#     def participants_list(self, obj):
#         return ", ".join([p.username for p in obj.participants.all()])
