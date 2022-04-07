from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import BuyCar


@receiver(post_save, sender=BuyCar)
def email_send(sender, instance, created, **kwargs):
    if created:
        subject = f'Buy Car by {instance.buy_name}'
        template = render_to_string('car/table_for_mail.html', {'buy_name': instance.buy_name, 'buy_mobile': instance.buy_mobile, 'seller_name': instance.car.seller_name, 'seller_mobile': instance.car.seller_mobile, 'make': instance.car.make,
                                                                'model': instance.car.model, 'Year': instance.car.year, 'condition': instance.car.condition, 'asking_price': instance.car.asking_price, 'commission_money': instance.commission_money, 'net_amount_seller': instance.net_amount_seller})
        msg = EmailMultiAlternatives(subject, template, settings.EMAIL_HOST_USER, [
            settings.EMAIL_HOST_USER])
        msg.content_subtype = 'html'
        msg.send()
