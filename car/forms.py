from django import forms

from .models import Car

rating = (('Poor', 'Poor'), ('Fair', 'Fair'),
          ('Good', 'Good'), ('Excellent', 'Excellent'))


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['id', 'seller_name', 'seller_mobile', 'make',
                  'model', 'year', 'condition', 'asking_price']


class BuyCarForm(forms.Form):
    buy_name = forms.CharField(max_length=255)
    buy_mobile = forms.CharField(max_length=20)
