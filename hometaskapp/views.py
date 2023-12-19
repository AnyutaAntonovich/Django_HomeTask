import logging

from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def index(request):
    logger.info('Page accessed')
    html = """
     <!doctype html>
     <html lang="en">
     <head>
     <title>Study Portal</title>
     </head>

     <body style="color:OrangeRed; background-color: DarkMagenta">
         <h1>Образовательный портал Study Portal</h1>
         <p style="color: Aqua">Oбразовательные услуги по различным направлениям.</p>
     </body>
     </html>
     """
    return HttpResponse(html)

def about_us(request):
    logger.info('Page accessed')
    html = """
    <!doctype html>
    <html lang="en">
    <head>
    <title>Study Portal - About Us</title>
    </head>

    <body style="color:OrangeRed; background-color: Chartreuse">
        <h1>Образовательный портал Study Portal</h1>
        <p>Мы предлагаем образовательные услуги по различным направлениям.</p>
        <p>Учиться совершенно не сложно, когда вас поддерживает Study Portal!</p>
        <p style="color:#ffffff">С нами вы сможете быстро и легко подтянуть знания по любому направлению и сдать все 
        экзамены на ОТЛИЧНО!
        </p>
    </body>
    </html>
    """
    return HttpResponse(html)
