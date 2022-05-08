from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Room, RoomReservation, Client, Images
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.utils.datastructures import MultiValueDictKeyError
from .name_upper import name_upper
from .tegram_bot import send_message
from datetime import datetime
# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'


def rooms(request):
    """View c описание доступных номеров"""
    room = Room.objects.all()
    images = Images.objects.filter(default_img=True)

    if request.method == 'GET':
        return render(request, 'rooms.html', {'room': room, 'images': images})


def room_details(request, pk):
    """View c описание доступных номеров"""
    room = Room.objects.get(pk=pk)
    images = Images.objects.filter(room_id=pk)

    if request.method == 'GET':
        return render(request, 'room_details.html', {'room': room, 'images': images})


def reserv(request):
    """View для бронирования"""
    room = Room.objects.all()
    images = Images.objects.filter(default_img=True)

    # print(room[0].type)
    if request.method == 'GET':
        return render(request, 'reservation.html', {'room': room, 'images': images})
    if request.method == 'POST':
        try:
            client_name = request.POST['client_name']
            client_phone = request.POST['client_phone']
            select_room = request.POST['select_room']
            date_in = request.POST['date_in']  # datetime.strptime(request.POST['date_in'], '%Y-%m-%d')
            date_out = request.POST['date_out']
            data_processing = request.POST['data_processing']  # checkbox в случае отсутствия --> MultiValueDictKeyError

            if client_name == '' or client_phone == '':
                raise ValidationError('Не указано имя или номер телефона')

            client_name = name_upper(client_name)
            client_phone = client_phone.replace(' ', '')
            select_room = images.get(src=f'core{select_room}')

            client = Client.objects.create(name=client_name, phone_number=client_phone)
            RoomReservation.objects.create(rooms=room.get(id=select_room.room_id), client=client,
                                           date_in=date_in, date_out=date_out)

            success_message = f'{client_name}, Ваша заявка зарегистрирована, мы позвоним Вам в ближайшее время :)'
            messages.success(request, success_message)

            # отправка уведомления о бронировании в телеграм
            notification_for_telegram = f'Заявка на бронирование! {client_name}, {client_phone}, ' \
                                        f'{select_room.room.type}, c {date_in} по {date_out}'
            send_message(notification_for_telegram)

        except MultiValueDictKeyError:  # check data_processing
            error_message = f'Без разрешения на обработку данных мы не можем создать заявку :('
            messages.error(request, error_message)
        except (ValidationError, Room.DoesNotExist):
            error_message = f'Произошла ошибка! Кажется вы заполнили не все поля!'
            messages.error(request, error_message)

        return render(request, 'reservation.html', {'room': room, 'images': images})


class Extra(TemplateView):

    template_name = 'extra.html'


def about_us(request):
    """View 'О нас'"""
    if request.method == 'GET':
        return render(request, 'about_us.html')
    if request.method == 'POST':
        try:
            client_name = request.POST['client_name']
            client_phone = request.POST['client_phone']

            if client_name == '' or client_phone == '':
                raise ValidationError('Не указано имя или номер телефона')
            client_name = name_upper(client_name)
            client_phone = client_phone.replace(' ', '')

            # отправка уведомления о запросе звонка в телеграм
            notification_for_telegram = f'Запрос звонка! {client_name}, {client_phone}'
            send_message(notification_for_telegram)

            success_message = f'{client_name}, мы позвоним Вам в ближайшее время :)'
            messages.success(request, success_message)

        except ValidationError:
            error_message = f'Произошла ошибка! Кажется Вы заполнили не все поля!'
            messages.error(request, error_message)

        return render(request, 'about_us.html')
