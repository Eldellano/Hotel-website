from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Room, RoomReservation, Client
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError
from .name_upper import name_upper
# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'


class AboutUs(TemplateView):

    template_name = 'about_us.html'


class Rooms(TemplateView):

    template_name = 'rooms.html'


# class Reserv(TemplateView):
#     template_name = 'reservation.html'


def reserv(request):
    room = Room.objects.all()
    # print(room[0].type)
    if request.method == 'GET':
        return render(request, 'reservation.html', {'room': room})
    if request.method == 'POST':
        try:
            client_name = request.POST['client_name']
            client_phone = request.POST['client_phone']
            select_room = request.POST['select_room']
            date_in = request.POST['date_in']
            date_out = request.POST['date_out']
            data_processing = request.POST['data_processing']

            if client_name == '' or client_phone == '':
                raise ValidationError('Не указано имя или номер телефона')

            client_name = name_upper(client_name)

            client = Client.objects.create(name=client_name, phone_number=client_phone)
            RoomReservation.objects.create(rooms=room.get(type=select_room), client=client,
                                           date_in=date_in, date_out=date_out)

            success_message = f'{client_name}, Ваша заявка зарегистрирована, мы позвоним Вам в ближайшее время :)'
            messages.success(request, success_message)

        except MultiValueDictKeyError:  # check data_processing
            error_message = f'Без разрешения на обработку данных мы не можем создать заявку :('
            messages.error(request, error_message)
        except (ValidationError, Room.DoesNotExist):
            error_message = f'Произошла ошибка! Кажется вы заполнили не все поля!'
            messages.error(request, error_message)

        return render(request, 'reservation.html', {'room': room})


class Extra(TemplateView):

    template_name = 'extra.html'
