from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import TransferForm
from .models import Transfer
from django.utils import timezone


@login_required(login_url='login')
def transferList(request):
    context = {
        'transfers': Transfer.objects.filter(sender=request.user)
    }
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
    context = {'form': form}
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
    print(transfer)
    context = {'transfer': transfer}
    return render(request, 'transferInfo.html', context)
