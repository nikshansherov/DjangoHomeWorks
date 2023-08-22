from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

TEXT1 = f'<h1>Я Николай, и это моя страничка</h><br>' \
        f'<a href="/about">О себе</a>'
TEXT2 = f'<h1>Я такой весь умный, красивый, а еще и скромный... ХА-ХА-ХА!!!</h><br>' \
        f'<a href="/">Главная</a>'


def index(request):
    return HttpResponse(TEXT1)


def about(request):
    return HttpResponse(TEXT2)
