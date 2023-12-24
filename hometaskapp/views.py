import logging

from django.http import HttpResponse
from django.shortcuts import render


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
