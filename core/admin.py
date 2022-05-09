from django.contrib import admin
from .models import Client, RoomReservation, Room, Images
# Register your models here.

admin.site.register(Client)
admin.site.register(RoomReservation)
admin.site.register(Room)


class ImagePreview(admin.ModelAdmin):
    readonly_fields = ["preview"]


admin.site.register(Images, ImagePreview)
