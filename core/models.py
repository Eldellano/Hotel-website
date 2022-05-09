from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class TimestampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Images(models.Model):
    alt = models.CharField(max_length=64, blank=True, verbose_name='Описание')
    src = models.ImageField(upload_to='core/static/img/rooms', verbose_name='Выбрать файл')
    room = models.ForeignKey('Room', null=True, blank=True, verbose_name='Номер', on_delete=models.CASCADE)
    default_img = models.BooleanField(default=False, verbose_name='Главная фотография')

    class Meta:
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.alt

    def preview(self):
        return mark_safe(f'<img src="{self.src.name[4:]}" style="max-height: 200px;">')
    preview.short_description = 'Предпросмотр'


class Room(models.Model):
    """Описание гостиничных номеров"""
    type = models.CharField(max_length=150, null=False, default='Номер', verbose_name='Тип номера')
    bed = models.PositiveIntegerField(null=False, verbose_name='Количество кроватей')
    floor = models.PositiveIntegerField(null=False, verbose_name='Этаж')
    cost_per_day = models.PositiveIntegerField(null=True, verbose_name='Стоимость за сутки')
    short_description = models.CharField(max_length=100, null=True, verbose_name='Короткое описание')
    description = models.CharField(max_length=300, null=True, verbose_name='Описание')
    # file will be uploaded to MEDIA_ROOT/uploads  #TODO: Почитать, настроить!
    # https://www.djbook.ru/rel1.9/ref/models/fields.html#filefield
    # photo = models.ImageField(upload_to='uploads/')

    class Meta:
        verbose_name_plural = 'Номера'

    def __str__(self):
        return self.type


class Client(models.Model):
    """Модель клиента"""
    name = models.CharField(max_length=200, null=False, verbose_name='Имя')
    phone_number = models.CharField(max_length=12, null=False, verbose_name='Номер телефона')
    city = models.CharField(max_length=150, null=True, blank=True, default='', verbose_name='Город')

    class Meta:
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        if self.city:
            return f'{self.name} - {self.city}'
        else:
            return self.name


class RoomReservation(TimestampedModel):
    """Добавление нового резервирования номера"""
    rooms = models.ForeignKey(Room, null=True, on_delete=models.SET_NULL, verbose_name='Номер')
    date_in = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата заезда')
    date_out = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата выезда')
    client = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL, verbose_name='Клиент')
    people_count = models.PositiveIntegerField(null=True, verbose_name='Количество людей')
    children = models.BooleanField(default=False, verbose_name='Есть ли дети')
    booking_confirmation = models.BooleanField(default=False, verbose_name='Резерв подтвержден')
    cost_estimate = models.PositiveIntegerField(null=True, blank=True, verbose_name='Стоимость проживания')

    class Meta:
        verbose_name_plural = 'Резервирование номеров'

    def __str__(self):
        return f'Клиент {self.client} c резервом номера {self.rooms}'

    # TODO: Вычисление стоимости сразу в поле: Rooms.cost_per_day * (date_out - date_in)
    # def get_cost(self):
    #     in_ = RoomReservation.date_in.date()
    #     out = RoomReservation.date_out.date()
    #     print(out)
    #     self.cost_estimate = out - in_
    #     self.save()
