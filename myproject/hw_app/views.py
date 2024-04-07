import logging
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .forms import ProductForm
from .models import Client, Order, OrderItem, Product
from django.utils import timezone
from datetime import timedelta

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

def orders_list(request):
    orders = Order.objects.filter(client=request.user.pk) 
    return render(request, 'hw_app/orders_list.html', {'orders': orders})

def orders_list_time(request, period):
    if period == 'week':
        start_date = timezone.now() - timedelta(days=7)
    elif period == 'month':
        start_date = timezone.now() - timedelta(days=30)
    elif period == 'year':
        start_date = timezone.now() - timedelta(days=365)
    
    order_items = OrderItem.objects.filter(order__client=request.user.pk, order__order_date__gte=start_date).order_by('order__order_date', 'product__name')
    
    unique_order_items = []
    seen = set()
    for order_item in order_items:
        if order_item.product.name not in seen:
            unique_order_items.append(order_item)
            seen.add(order_item.product.name)
    
    return render(request, 'hw_app/ordered_products_list.html', {'order_items': unique_order_items})

def edit_product(request):      
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                price = form.cleaned_data['price']
                quantity = form.cleaned_data['quantity']
                added_date = form.cleaned_data['added_date']
                photo = form.cleaned_data['photo']
                product = Product(name=name, description=description, price=price, quantity=quantity, added_date=added_date, photo=photo)
                product.save()
                message = 'Продукт изменен'
            else:
                message = 'Некорректные данные'
        else:
            form = ProductForm()
            message = 'Введите данные'
        return render(request, 'hw_app/edit_product.html', {'form': form, 'message': message})