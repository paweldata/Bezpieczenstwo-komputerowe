from django.urls import path
from transfer import views


urlpatterns = [
    path('list/', views.transferList, name='transferList'),
    path('prepare/', views.prepareTransfer, name='prepareTransfer'),
    path('confirm/', views.confirmTransfer, name='confirmTransfer'),
    path('send/', views.sendTransfer, name='sendTransfer'),
    path('info/', views.showTransfer, name='infoTransfer')
]
