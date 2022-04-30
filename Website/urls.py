"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import IndexView, Rooms, Extra, reserv, about_us

urlpatterns = [
    path('', IndexView.as_view()),
    path('rooms/', Rooms.as_view(), name='rooms'),
    path('reservation/', reserv, name='reservation'),
    path('extra/', Extra.as_view(), name='extra'),
    path('about_us/', about_us, name='about_us'),
    path('admin/', admin.site.urls),
]
