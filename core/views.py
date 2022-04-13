from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.


class IndexView(TemplateView):

    template_name = 'index.html'


class AboutUs(TemplateView):

    template_name = 'about_us.html'


class Rooms(TemplateView):

    template_name = 'rooms.html'


class Reserv(TemplateView):

    template_name = 'reservation.html'


class Extra(TemplateView):

    template_name = 'extra.html'
