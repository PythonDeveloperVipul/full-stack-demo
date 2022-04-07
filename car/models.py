import datetime

from django.core.validators import RegexValidator
from django.db import models
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.money import Money

condition = (('Poor', 'Poor'), ('Fair', 'Fair'),
             ('Good', 'Good'), ('Excellent', 'Excellent'))
year_choices = [(r, r) for r in range(2000, datetime.date.today().year+1)]
car_status = (('Available', 'Available'), ('Sold', 'Sold'))
phoneNumberRegex = RegexValidator(regex=r"^\+?1?\d{8,15}$")


class Car(models.Model):
    seller_name = models.CharField(max_length=255)
    seller_mobile = models.CharField(
        max_length=20, validators=[phoneNumberRegex])
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField(
        ('year'), choices=year_choices, default=datetime.date.today().year)
    condition = models.CharField(max_length=20, choices=condition)
    asking_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', validators=[MinMoneyValidator(Money(1000, 'USD')),
                                                                                                   MaxMoneyValidator(Money(100000, 'USD')), ])
    car_status = models.CharField(
        max_length=20, default='Available', choices=car_status)

    class Meta:
        verbose_name_plural = 'Sell Cars'

    def __str__(self):
        return self.seller_name


class BuyCar(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    buy_name = models.CharField(max_length=255)
    buy_mobile = models.CharField(max_length=20, validators=[phoneNumberRegex])
    commission_money = MoneyField(
        max_digits=14, decimal_places=2, default_currency='USD', default=0)
    net_amount_seller = MoneyField(
        max_digits=14, decimal_places=2, default_currency='USD', default=0)

    @property
    def get_commission_money(self):
        total = ((self.car.asking_price*5)/100)
        return total

    @property
    def get_net_amount_seller(self):
        total = ((self.car.asking_price*5)/100)
        net_amout = (self.car.asking_price - total)
        return net_amout

    def save(self, *args, **kwargs):
        self.commission_money = self.get_commission_money
        self.net_amount_seller = self.get_net_amount_seller
        super(BuyCar, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Buy Cars'
