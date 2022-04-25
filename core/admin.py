from django.contrib import admin
from .models import Client, RoomReservation, Room, Images
# Register your models here.

admin.site.register(Client)
admin.site.register(RoomReservation)
admin.site.register(Room)
admin.site.register(Images)
