# Generated by Django 3.1.4 on 2021-01-07 20:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0002_auto_20210101_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='recipientAccount',
            field=models.CharField(max_length=26, validators=[django.core.validators.RegexValidator(message='Account should be 26 digit number', regex='[0-9]{26}')]),
        ),
    ]
