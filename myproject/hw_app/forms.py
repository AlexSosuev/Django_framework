import datetime
from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Название товара', max_length=100)
    price = forms.DecimalField(label='Цена', max_digits=9, decimal_places=2)
    description = forms.CharField(label='Описание')
    quantity = forms.IntegerField(label='Количество')
    added_date = forms.DateField(label='Дата добавления', initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    photo = forms.ImageField(label='Фотография товара')