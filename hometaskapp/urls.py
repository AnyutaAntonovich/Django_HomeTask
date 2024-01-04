from django.urls import path
from .views import index, about_us, data_time


urlpatterns = [
   path('', index, name='index'),
   path('about/', about_us, name='about_us'),
   path('data_time/', data_time, name='data_time'),
]
