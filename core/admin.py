from django.contrib import admin
from .models import Client, RoomReservation, Room
# Register your models here.

admin.site.register(Client)
admin.site.register(RoomReservation)
admin.site.register(Room)
