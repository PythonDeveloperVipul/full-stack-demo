# Generated by Django 4.0.2 on 2022-04-04 04:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_alter_car_car_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='buycar',
            options={'verbose_name_plural': 'Buy Cars'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name_plural': 'Sell Cars'},
        ),
        migrations.AlterField(
            model_name='buycar',
            name='buy_mobile',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
        migrations.AlterField(
            model_name='car',
            name='seller_mobile',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')]),
        ),
    ]
