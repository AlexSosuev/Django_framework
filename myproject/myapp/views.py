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
    
def coin(request, num):
    result = [choice(['orel', 'reshka']) for _ in range(num)]
    context = {'result': result}
    return render(request, 'myapp/games.html', context)

def cube(request, num):
    result = [randint(1, 6) for _ in range(num)]
    context = {'result': result}
    return render(request, 'myapp/games.html', context)

def number(request, num):
    result = [randint(1, 100) for _ in range(num)]
    context = {'result': result}
    return render(request, 'myapp/games.html', context)

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
    
def index(request):
    context = {
        'title': 'Главная',
        'message': 'Это главная страница'
    }
    return render(request, 'myapp/index.html', context)

def about(request):
    context = {
        'title': 'О нас',
        'message': 'Это страница о ...'
    }
    return render(request, 'myapp/about.html', context)