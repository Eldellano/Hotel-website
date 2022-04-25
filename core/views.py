from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Room, RoomReservation, Client
# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'


class AboutUs(TemplateView):

    template_name = 'about_us.html'


class Rooms(TemplateView):

    template_name = 'rooms.html'


class Reserv(TemplateView):
    template_name = 'reservation.html'


def reserv(request):
    room = Room.objects.all()
    # print(room[0].type)
    if request.method == 'GET':
        return render(request, 'reservation.html', {'room': room})
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_phone = request.POST['client_phone']
        select_room = request.POST['select_room']
        date_in = request.POST['date_in']
        date_out = request.POST['date_out']

        client = Client.objects.create(name=client_name, phone_number=client_phone)
        RoomReservation.objects.create(rooms=room.get(type=select_room), client=client,
                                       date_in=date_in, date_out=date_out)

        return render(request, 'reservation.html', {'room': room})




class Extra(TemplateView):

    template_name = 'extra.html'
