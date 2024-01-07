from django.urls import path
from .views import index, about_us, data_time, upload_image


urlpatterns = [
   path('', index, name='index'),
   path('about/', about_us, name='about_us'),
   path('data_time/', data_time, name='data_time'),
   path('upload/', upload_image, name='upload_image')
]
