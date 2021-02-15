from django.urls import path
from webpage import views

urlpatterns = [
    path('', views.main, name='index'),
]
