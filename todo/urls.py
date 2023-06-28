from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user/signup/', views.sign_up, name='sign_up'),
    path('user/login/', views.log_in, name='log_in'),
    path('user/logout/', views.log_out, name='logout')
]