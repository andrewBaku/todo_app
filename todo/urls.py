from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('user/signup/', views.sign_up, name='sign_up'),
    path('user/login/', views.log_in, name='log_in'),
    path('user/logout/', views.log_out, name='logout'),
    path('task/create/', views.create_task, name='create_task'),
    path('task/<int:pk>/detail/', views.task_detail, name='task_detail'),
    path('task/<int:pk>/done/', views.done_task, name='done_task'),
    path('task/<int:pk>/cancel/', views.cancel_task, name='cancel_task'),
]