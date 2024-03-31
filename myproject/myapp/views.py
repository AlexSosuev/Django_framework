import random
from django.shortcuts import render
from random import choice, randint
from .models import Games, Author_2
from datetime import date

import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page accessed')
    return HttpResponse('Hello, world')

def about(request):
    try:
        result = 1/0
    except Exception as e:
        logger.exception(f'Error in about page: {e}')
        return HttpResponse('Oops, something went wrong.')
    else:
        logger.debug('About page acceessed')
        return HttpResponse('This is the about page.')
    
# Создайте новое приложение. Подключите его к проекту. В приложении должно быть три простых представления, возвращающих HTTP ответ:
# 1. Орёл или решка
# 2. Значение одной из шести граней игрального кубика
# 3. Случайное число от 0 до 100
# Пропишите маршруты
    

# Добавьте логирование в проект. Настройте возможность вывода в файл и в терминал. Устраните возможные ошибки.
# *Форматирование настройте по своему желанию. Объясните что вы выводите в логи
    
def coin(request):
    result = choice(['orel', 'reshka'])
    logger.info(f'result = {result}')
    return HttpResponse(result)

def cube(request):
    return HttpResponse(randint(1, 6))

def number(request):
    return HttpResponse(randint(1, 100))

def game(request):
    coin_side = random.choice(['head', 'tail'])
    game = Games(side=coin_side)
    game.save()
    return HttpResponse(coin_side)

def statistics(request):
    data = Games.stat_game()
    return HttpResponse(f'{data}')

def create_authors(request):
    result=[]
    for i in range(10):
        author = Author_2(name=f'name{i}', lastname=f'lastname{i}', email = f'email{i}', biography = f'biography{i}', birthday=date.today())
        author.save()
        result.append(author.fullname())
    return HttpResponse(f'{result}')
    