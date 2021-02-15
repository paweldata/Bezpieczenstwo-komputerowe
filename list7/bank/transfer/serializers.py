from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Transfer


class TransfersHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transfer
        fields = ('recipientName', 'recipientAccount', 'title', 'amount', 'date')


class TransferSendingSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.SerializerMethodField('_user')

    def _user(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user.id

    class Meta:
        model = Transfer
        fields = ('sender', 'recipientName', 'recipientAccount', 'title', 'amount', 'date')


class TransferConfirmedSerializer(serializers.HyperlinkedModelSerializer):
    sender = serializers.SerializerMethodField('_user')

    def _user(self, obj):
        request = getattr(self.context, 'request', None)
        if request:
            return request.user.id

    class Meta:
        model = Transfer
        fields = ('sender', 'recipientName', 'recipientAccount', 'title', 'amount', 'date')
