from django import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='car_sell_list'),
    path('car_add/', views.CarCreateView.as_view(), name='car_data_insert'),
    path('thankspage/', views.ThanksPage.as_view(), name='thanks_page'),
    path('buycar/<int:pk>', views.BuyCarView.as_view(), name='buycar'),
    path('car-status-change/<int:pk>',
         views.CarStatusChange.as_view(), name='car_status_change'),
]
