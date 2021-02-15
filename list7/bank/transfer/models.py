from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_account(value):
    compare = re.compile('[0-9]{26}')
    if not compare.match(value):
        raise ValidationError('Account should be 26 digit number')


class Transfer(models.Model):
    sender = models.ForeignKey(User, null=False, editable=False, on_delete=models.CASCADE)
    recipientAccount = models.CharField(null=False, blank=False, max_length=26, validators=[validate_account])
    recipientName = models.CharField(null=False, blank=False, max_length=300)
    title = models.CharField(null=False, blank=False, max_length=120)
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    date = models.DateTimeField(default=timezone.now)
    isConfirmed = models.BooleanField(default=False)
