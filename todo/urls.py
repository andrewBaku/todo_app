from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.first_page, name='home'),
    path('user/signup/', views.sign_up, name='sign_up'),
]