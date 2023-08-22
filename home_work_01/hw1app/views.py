from django.shortcuts import render
from django.http import HttpResponse
import logging
from random import randint, choice

logger = logging.getLogger(__name__)

TEXT1 = f'<h1>Я Николай, и это моя страничка<br>Здесь вроде бы как ' \
        f'расположен многострочный текст :)</h><br>' \
        f'<a href="/about">О себе</a><br>' \
        f'<a href="/games">Поиграй</a>'
TEXT2 = f'<h1>Я такой весь умный, красивый, а еще и скромный... ХА-ХА-ХА!!!</h><br>' \
        f'<a href="/">Главная</a><br>' \
        f'<a href="/games">Поиграй</a>'
TEXT3 = f'<h1>Выбирете игру</h><br>' \
        f'<a href="/cube">Бросить кубик<br></a>' \
        f'<a href="/heads_or_tails">Орел или решка<br></a>' \
        f'<a href="/random_number">Случайное число<br></a>' \
        f'<a href="/">Главная</a>'


def index(request):
    return HttpResponse(TEXT1)


def about(request):
    return HttpResponse(TEXT2)


def games(request):
    return HttpResponse(TEXT3)


def cube(request):
    number = randint(1, 6)
    logger.info(f'Result - {number}')
    return HttpResponse(f'<h1>Ваш бросок кубика - {number}</h><br>'
                        f'<a href="/games">Вернуться</a><br>')


def heads_or_tails(request):
    cast = choice(['Орел', 'Решка'])
    logger.info(f'Result - {cast}')
    return HttpResponse(f'<h1>Вы бросили - {cast}</h><br>'
                        f'<a href="/games">Вернуться</a><br>')


def random_number(request):
    number = randint(0, 100)
    logger.info(f'Result - {number}')
    return HttpResponse(f'<h1>Ваше число - {number}</h><br>'
                        f'<a href="/games">Вернуться</a><br>')

