import logging

from django.http import HttpResponse
from django.shortcuts import render
import datetime


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Page accessed')
    name = 'Study Portal'
    adress = 'Kamzina 85'
    context = {'name': name, 'adress': adress}
    return render(request, 'hometaskapp/index.html', context=context)


def about_us(request):
    logger.info('Page accessed')
    name = 'Study Portal'
    adress = 'Kamzina 85'
    type_ = 'Education'
    context = {'name': name, 'adress': adress, 'type_': type_}
    return render(request, 'hometaskapp/about_us.html', context=context)


def data_time(request):
    logger.info('Page accessed')
    delta_week = datetime.timedelta(days=7)
    delta_month = datetime.timedelta(days=30)
    delta_year = datetime.timedelta(days=365)

    context = {'delta_week': delta_week, 'delta_month': delta_month, 'delta_year': delta_year}
    return render(request, 'hometaskapp/data_time.html', context=context)
