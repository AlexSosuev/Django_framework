import logging
from django.shortcuts import render
from django.http import HttpResponse
from .models import Client

# Create your views here.
logger = logging.getLogger(__name__)

def main(request):
    main_html = """
    <!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>GB-Django</title>
  </head>
  <body>
    <h1>Мой первый Django-сайт.</h1>
    <p>Привет, это мой учебный проект на Django.</p>
  </body>
</html>
    """
    logger.info('Открыта страница MAIN')
    return HttpResponse(main_html)

def about_me(request):
    about_me_html = """
    <!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>О себе</title>
  </head>
  <body>
    <h1>Привет, это мой учебный проект на Django.</h1>
    <p>Всем привет!</p>
    <p>Меня зовут Александр и это мой первый проект на Django.</p>
    <h2>Немного о себе:</h2>
    <p>
      Я - вечный студент))
    </p>   
  </body>
</html>
    """
    logger.info('Открыта страница ABOUT_ME')
    return HttpResponse(about_me_html)

def create_client(name, email, phone_number, address, registration_date):
    client = Client(name=name, email=email, phone_number=phone_number, address=address, registration_date=registration_date)
    client.save()
    logger.info('Клиент добавлен!')
    return HttpResponse(client)

def update_client(client_id, name=None, email=None, phone_number=None, address=None, registration_date=None):
    client = Client.objects.get(pk=client_id)
    if name:
        client.name = name
    if email:
        client.email = email
    if phone_number:
        client.phone_number = phone_number
    if address:
        client.address = address
    if registration_date:
        client.registration_date = registration_date
    client.save()
    logger.info('Клиент изменен!')
    return HttpResponse(client)

def delete_client(client_id):
    client = Client.objects.get(pk=client_id)
    client.delete()
    logger.info('Клиент удален!')
    return HttpResponse(client)