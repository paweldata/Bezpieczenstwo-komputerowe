from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import connection

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse

from.serializers import *

from .forms import TransferForm
from .models import Transfer


@login_required(login_url='login')
def transferList(request):
    context = {
        'transfers': Transfer.objects.filter(sender=request.user)
    }
    return render(request, 'transferList.html', context)


@login_required(login_url='login')
def filterTransfers(request):
    context = {
        'transfers': Transfer.objects.raw(
            'SELECT * '
            'FROM transfer_transfer '
            'WHERE sender_id = ' + str(request.user.id) +
            ' AND recipientName LIKE "%%' + str(request.POST['recipientName']) + '%%"'),
    }

    if request.POST['query']:
        with connection.cursor() as c:
            c.execute(str(request.POST['query']))
            context['queryResult'] = c.fetchall()

    print(context['transfers'])
    return render(request, 'transferList.html', context)


@login_required(login_url='login')
def prepareTransfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
    else:
        form = TransferForm()
    form.setReadOnly(False)
    context = {'form': form}
    return render(request, 'transferPrepare.html', context)


@login_required(login_url='login')
def confirmTransfer(request):
    form = TransferForm(request.POST)

    if not form.is_valid():
        messages.info(request, 'Account should be 26 digit number')
        form.setReadOnly(False)
        context = {'form': form}
        return render(request, 'transferPrepare.html', context)

    form.setReadOnly(True)

    context = {
        'form': form
    }

    return render(request, 'transferConfirm.html', context)


@login_required(login_url='login')
def sendTransfer(request):
    form = TransferForm(request.POST)
    transfer = form.save(commit=False)
    transfer.sender = request.user
    transfer.save()
    return redirect('infoTransfer')


@login_required(login_url='login')
def showTransfer(request):
    transfer = Transfer.objects.filter(sender=request.user).order_by('-id')[0]
    context = {'transfer': transfer}
    return render(request, 'transferInfo.html', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_superuser)
def adminPage(request):
    context = {
        'transfers': Transfer.objects.filter(isConfirmed=False)
    }

    return render(request, 'adminConfirmTransfers.html', context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_superuser)
def adminConfirmTransfers(request):
    transfers = Transfer.objects.filter(isConfirmed=False)
    for transfer in transfers:
        transfer.isConfirmed = True
        transfer.save()

    context = {
        'transfers': Transfer.objects.filter(isConfirmed=False)
    }
    return render(request, 'adminConfirmTransfers.html', context)


@api_view(['GET'])
@authentication_classes((JWTAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated,))
def apiTransferList(request):
    print("ApiTransferList")
    if request.method == 'GET':
        print(request.user.id)
        transfers = []
        for item in Transfer.objects.all():
            if item.sender_id == request.user.id:
                transfers.append(item)

        serializer = TransfersHistorySerializer(transfers, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
@authentication_classes((JWTAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated, ))
def apiSendTransfer(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TransferSendingSerializer(data=data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
