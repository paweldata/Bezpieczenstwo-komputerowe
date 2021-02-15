from django.forms import ModelForm, Form, CharField
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

from .models import Transfer


class TransferForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TransferForm, self).__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['readonly'] = True

    class Meta:
        model = Transfer
        fields = ['recipientName', 'recipientAccount', 'title', 'amount', 'date', 'isConfirmed']

    def setReadOnly(self, readOnly):
        self.fields['recipientName'].widget.attrs['readonly'] = readOnly
        self.fields['recipientAccount'].widget.attrs['readonly'] = readOnly
        self.fields['title'].widget.attrs['readonly'] = readOnly
        self.fields['amount'].widget.attrs['readonly'] = readOnly
