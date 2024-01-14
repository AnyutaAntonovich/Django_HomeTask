import logging

from django.shortcuts import render
import datetime
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm


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


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'hometaskapp/upload_image.html', {'form': form})
