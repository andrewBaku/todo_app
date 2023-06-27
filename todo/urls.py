from django.urls import path, include
from .views import *


urlpatterns = [
    path('', first_page, name='first_page'),
]