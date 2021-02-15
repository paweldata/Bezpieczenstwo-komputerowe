from django.urls import path
from transfer import views


urlpatterns = [
    path('list/', views.transferList, name='transferList'),
    path('filter/', views.filterTransfers, name='filterTransfer'),
    path('prepare/', views.prepareTransfer, name='prepareTransfer'),
    path('confirm/', views.confirmTransfer, name='confirmTransfer'),
    path('send/', views.sendTransfer, name='sendTransfer'),
    path('info/', views.showTransfer, name='infoTransfer'),
    path('admin/', views.adminPage, name='adminPage'),
    path('admin/confirm/', views.adminConfirmTransfers, name='adminConfirm'),

    path('api/list/', views.apiTransferList, name='ApiTransferList'),
    path('api/prepare/', views.apiSendTransfer, name='ApiPrepareTransfer'),
]
