from django.urls import path
from . import views


urlpatterns = [
    path('coin/<int:count>', views.coin, name='coin'),
    path('dice/', views.dice, name='dice'),
    path('random_number/<int:count>/', views.random_number, name='random_number'),
    path('log_main/', views.log_main, name='log_main'),
    path('log_page/', views.log_page, name='log_page'),
    path('cihoise_game/', views.cihoise_game, name='cihoise_game'),
]