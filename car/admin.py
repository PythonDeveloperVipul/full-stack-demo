from django.contrib import admin

from .models import BuyCar, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['seller_name', 'seller_mobile', 'make',
                    'year', 'condition', 'asking_price', 'car_status']


@admin.register(BuyCar)
class CarBuyAdmin(admin.ModelAdmin):
    list_display = ['buy_name', 'buy_mobile',
                    'commission_money', 'net_amount_seller']
