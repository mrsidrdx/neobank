from django.urls import path
from .views import index, about, blog, news_event, manageexpenses, contact, wealth, services

app_name = 'frontend'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('blog/', blog, name='blog'),
    path('news-event/', news_event, name='news_event'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('services/employee/manageexpenses/', manageexpenses, name='services_manageexpenses'),
    path('services/employee/wealth/', wealth, name='services_wealth'),
]
